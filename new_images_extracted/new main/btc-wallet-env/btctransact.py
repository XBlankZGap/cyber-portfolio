from bitcoin import *
import requests
import pyfiglet

def show_banner():
    ascii_banner = pyfiglet.figlet_format("SOPHY BTC")
    print(ascii_banner)

def get_balance(address):
    try:
        url = f"https://blockchain.info/balance?active={address}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[address]
        return data['final_balance'] / 100000000  # Convert satoshis to BTC
    except Exception as e:
        print(f"Error fetching balance for {address}: {e}")
        return None

def check_multiple_balances():
    print("Enter Bitcoin addresses separated by commas:")
    addresses = input("Addresses: ").split(',')

    for addr in addresses:
        addr = addr.strip()
        balance = get_balance(addr)
        if balance is not None:
            print(f"{addr}: {balance:.8f} BTC")
        else:
            print(f"{addr}: Error retrieving balance")

def broadcast_tx(raw_tx_hex):
    url = 'https://api.blockcypher.com/v1/btc/main/txs/push'
    payload = {"tx": raw_tx_hex}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        tx_hash = response.json().get('tx', {}).get('hash')
        print(f"\nTransaction broadcasted successfully!\nTXID: {tx_hash}")
        return tx_hash
    except Exception as e:
        print(f"\nBroadcast failed: {e}")
        print("Response:", response.text if response else "No response")
        return None

def send_transaction():
    print("Send Bitcoin")
    wif_key = input("Enter your WIF private key: ").strip()
    recipient = input("Recipient Bitcoin address: ").strip()
    amount_btc = float(input("Amount to send (BTC): ").strip())
    fee_btc = float(input("Transaction fee (BTC): ").strip())

    try:
        # Derive address and pubkey
        sender_pub = privtopub(wif_key)
        sender_addr = pubtoaddr(sender_pub)

        print(f"\nSender Address: {sender_addr}")

        # Fetch UTXOs
        url = f"https://blockchain.info/unspent?active={sender_addr}"
        response = requests.get(url)
        response.raise_for_status()
        utxos = response.json()['unspent_outputs']

        inputs = []
        total_input = 0
        for utxo in utxos:
            inputs.append({
                'output': f"{utxo['tx_hash_big_endian']}:{utxo['tx_output_n']}",
                'value': utxo['value']
            })
            total_input += utxo['value']
            if total_input >= (amount_btc + fee_btc) * 100000000:
                break

        if total_input < (amount_btc + fee_btc) * 100000000:
            print("Insufficient balance.")
            return

        outputs = [
            (recipient, int(amount_btc * 100000000))
        ]
        change = total_input - int((amount_btc + fee_btc) * 100000000)
        if change > 0:
            outputs.append((sender_addr, change))

        tx = mktx([i['output'] for i in inputs], outputs)
        for i in range(len(inputs)):
            tx = sign(tx, i, wif_key)

        print("\nRaw Signed Transaction (Hex):")
        print(tx)

        # Auto broadcast
        broadcast_tx(tx)

    except Exception as e:
        print(f"Transaction creation failed: {e}")

def main():
    show_banner()
    while True:
        print("\nBitcoin Wallet Tools")
        print("1. Check balance of multiple addresses")
        print("2. Send transaction")
        print("3. Exit")

        option = input("Select option: ")

        if option == '1':
            check_multiple_balances()
        elif option == '2':
            send_transaction()
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

