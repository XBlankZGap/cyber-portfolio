#!/usr/bin/env python3

import pyfiglet
from bip_utils import (
    Bip39SeedGenerator,
    Bip44,
    Bip44Coins,
    Bip44Changes,
    Bip84,
    Bip84Coins
)

def print_banner():
    banner = pyfiglet.figlet_format("Z E T A Y O T A")
    print(banner)

def prompt_mnemonic():
    mnemonic = input("Enter your 12-word mnemonic phrase: ").strip()
    return mnemonic

def prompt_coin():
    print("Select coin to derive addresses for:")
    print("1. Bitcoin (BTC)")
    print("2. Ethereum (ETH)")
    choice = input("Enter choice number (1 or 2): ").strip()
    if choice == '1':
        return 'bitcoin'
    elif choice == '2':
        return 'ethereum'
    else:
        print("Invalid choice, defaulting to Bitcoin")
        return 'bitcoin'

def prompt_btc_address_type():
    print("Select Bitcoin address type:")
    print("1. Legacy (P2PKH) - addresses start with '1'")
    print("2. Native SegWit (P2WPKH) - addresses start with 'bc1'")
    choice = input("Enter choice number (1 or 2): ").strip()
    if choice == '1':
        return 'legacy'
    elif choice == '2':
        return 'segwit'
    else:
        print("Invalid choice, defaulting to Legacy")
        return 'legacy'

def derive_addresses_with_keys(mnemonic, coin, btc_addr_type='legacy', count=5):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    if coin == 'bitcoin':
        if btc_addr_type == 'legacy':
            bip_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
        elif btc_addr_type == 'segwit':
            bip_mst = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
        else:
            raise ValueError("Unsupported Bitcoin address type")
    elif coin == 'ethereum':
        bip_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    else:
        raise ValueError("Unsupported coin")

    print(f"\nDerived {count} {coin.upper()} addresses and private keys ({btc_addr_type if coin=='bitcoin' else 'standard'}):")
    print("-" * 80)
    for i in range(count):
        addr_obj = bip_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
        address = addr_obj.PublicKey().ToAddress()
        if coin == 'bitcoin':
            priv_key = addr_obj.PrivateKey().ToWif()
        elif coin == 'ethereum':
            priv_key = addr_obj.PrivateKey().Raw().ToHex()
        print(f"{i+1}:")
        print(f"  Address:    {address}")
        print(f"  PrivateKey: {priv_key}")
        print()
    print("-" * 80)

def main():
    print_banner()
    mnemonic = prompt_mnemonic()
    coin = prompt_coin()
    btc_addr_type = 'legacy'
    if coin == 'bitcoin':
        btc_addr_type = prompt_btc_address_type()
    try:
        derive_addresses_with_keys(mnemonic, coin, btc_addr_type)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

