#!/usr/bin/env python3

import hashlib
import hmac
import ecdsa
import argparse
import sys
import os
import pyfiglet

# Base58 implementation (to avoid external dependency)
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58encode(byte_str):
    """Encode bytes to base58"""
    n = int.from_bytes(byte_str, 'big')
    base58 = ''
    while n > 0:
        n, mod = divmod(n, 58)
        base58 = BASE58_ALPHABET[mod] + base58
    # Add leading '1's for zero bytes
    leading_zeros = len(byte_str) - len(byte_str.lstrip(b'\x00'))
    return '1' * leading_zeros + base58

# Constants
BIP39_PBKDF2_ROUNDS = 2048
BIP39_SALT_MODIFIER = "mnemonic"
BITCOIN_SEED = "Bitcoin seed"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    ascii_banner = pyfiglet.figlet_format("ZETAYOTA KEYGEN")
    print(ascii_banner)

def bip39_to_seed(mnemonic, passphrase=""):
    """Convert BIP39 mnemonic to seed"""
    mnemonic_bytes = mnemonic.encode("utf-8")
    salt = (BIP39_SALT_MODIFIER + passphrase).encode("utf-8")
    return hashlib.pbkdf2_hmac("sha512", mnemonic_bytes, salt, BIP39_PBKDF2_ROUNDS)

def create_master_key(seed):
    """Create BIP32 master key from seed"""
    h = hmac.new(BITCOIN_SEED.encode(), seed, hashlib.sha512).digest()
    private_key, chain_code = h[:32], h[32:]
    return private_key, chain_code

def derive_child_key(private_key, chain_code, index):
    """Derive child key using BIP32"""
    index_bytes = index.to_bytes(4, byteorder='big')
    h = hmac.new(chain_code, private_key + index_bytes, hashlib.sha512).digest()
    child_private = (int.from_bytes(h[:32], 'big') + int.from_bytes(private_key, 'big')) % ecdsa.SECP256k1.order
    child_private = child_private.to_bytes(32, 'big')
    child_chain_code = h[32:]
    return child_private, child_chain_code

def private_to_wif(private_key, compressed=True, testnet=False):
    """Convert private key to WIF format"""
    prefix = b'\xef' if testnet else b'\x80'
    suffix = b'\x01' if compressed else b''
    extended = prefix + private_key + suffix
    checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
    return base58encode(extended + checksum)

def private_to_address(private_key, testnet=False):
    """Convert private key to Bitcoin address"""
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = b'\x04' + vk.to_string()
    
    # SHA-256 then RIPEMD-160
    sha256 = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    
    # Add network byte
    prefix = b'\x6f' if testnet else b'\x00'
    extended = prefix + ripemd160
    
    # Checksum
    checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
    return base58encode(extended + checksum)

def derive_from_path(mnemonic, path="m/44'/0'/0'/0/0", testnet=False):
    """Derive key from BIP32 path"""
    seed = bip39_to_seed(mnemonic)
    private_key, chain_code = create_master_key(seed)
    
    for index in parse_path(path):
        private_key, chain_code = derive_child_key(private_key, chain_code, index)
    
    wif = private_to_wif(private_key, testnet=testnet)
    address = private_to_address(private_key, testnet=testnet)
    return {
        'private_key': wif,
        'address': address
    }

def parse_path(path):
    """Parse BIP32 path string into indices"""
    if not path.startswith('m'):
        raise ValueError("Path must start with 'm'")
    
    indices = []
    for level in path.split('/')[1:]:
        if level.endswith("'"):
            indices.append(0x80000000 + int(level[:-1]))
        else:
            indices.append(int(level))
    return indices

def list_addresses(mnemonic, count=5, testnet=False):
    """List addresses from mnemonic"""
    addresses = []
    for i in range(count):
        path = f"m/44'/1'/0'/0/{i}" if testnet else f"m/44'/0'/0'/0/{i}"
        key_info = derive_from_path(mnemonic, path, testnet)
        addresses.append({
            'index': i,
            'address': key_info['address'],
            'private_key': key_info['private_key']
        })
    return addresses

def main():
    parser = argparse.ArgumentParser(description='ZETAYOTA KEYGEN - Blockchain Wallet Recovery')
    parser.add_argument('--mnemonic', type=str, help='12-word recovery phrase')
    parser.add_argument('--testnet', action='store_true', help='Use testnet')
    
    args = parser.parse_args()
    
    if not args.mnemonic:
        clear_screen()
        show_banner()
        args.mnemonic = input("Enter your 12-word recovery phrase: ").strip()
    
    try:
        while True:
            clear_screen()
            show_banner()
            print("\nMenu Options:")
            print("1. List addresses and private keys")
            print("2. Get specific address")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                clear_screen()
                show_banner()
                count = input("How many addresses to display? (default 5): ") or 5
                try:
                    count = int(count)
                    addresses = list_addresses(args.mnemonic, count, args.testnet)
                    print("\nAddresses and Private Keys:")
                    print("-" * 90)
                    print(f"{'Index':<6} {'Address':<42} {'Private Key (WIF)':<52}")
                    print("-" * 90)
                    for addr in addresses:
                        print(f"{addr['index']:<6} {addr['address']:<42} {addr['private_key']:<52}")
                    print("-" * 90)
                    input("\nPress Enter to continue...")
                except ValueError:
                    print("Invalid number entered")
                    input("\nPress Enter to continue...")
            
            elif choice == '2':
                clear_screen()
                show_banner()
                index = input("Enter address index (default 0): ") or 0
                try:
                    index = int(index)
                    path = f"m/44'/1'/0'/0/{index}" if args.testnet else f"m/44'/0'/0'/0/{index}"
                    key_info = derive_from_path(args.mnemonic, path, args.testnet)
                    print("\nAddress Information:")
                    print("-" * 64)
                    print(f"Index:       {index}")
                    print(f"Address:     {key_info['address']}")
                    print(f"Private Key: {key_info['private_key']}")
                    print("-" * 64)
                    input("\nPress Enter to continue...")
                except ValueError:
                    print("Invalid index entered")
                    input("\nPress Enter to continue...")
            
            elif choice == '3':
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice, please try again")
                input("\nPress Enter to continue...")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()

