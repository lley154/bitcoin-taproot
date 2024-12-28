from bip32utils import BIP32Key
from mnemonic import Mnemonic
import hashlib
import base58  # You might need to install this: pip install base58
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Generate private key from seed phrase')
parser.add_argument('--seed', type=str, required=True, help='Must use seed phrase')
args = parser.parse_args()


# Your seed phrase from step 1
#seed_phrase = "sister object cereal ride sniff yellow virus brief work merry employ flat west arch live curious come magnet advice chalk steel chief grab promot"
seed_phrase = args.seed
# Convert seed phrase to seed
mnemo = Mnemonic("english")
seed = mnemo.to_seed(seed_phrase)

# Derive the master key (m)
master_key = BIP32Key.fromEntropy(seed)

# Derive path m/44'/0'/0'/0/0 (first receiving address)
# 44' = BIP44
# 1'  = Bitcoin Testnet (0 Bitcoin Mainnet)
# 0'  = First account
# 0   = External chain (receiving)
# 0   = First address index
derived_key = master_key.ChildKey(44 + 0x80000000)\
                       .ChildKey(1 + 0x80000000)\
                       .ChildKey(0 + 0x80000000)\
                       .ChildKey(0)\
                       .ChildKey(0)

# Mainnet
#print("Private key (WIF):", derived_key.WalletImportFormat())

# Testnet
def to_testnet_wif(private_key_bytes):
    """Convert raw private key bytes to testnet WIF format"""
    # Add testnet version byte (0xEF)
    version = bytes([0xEF])
    extended_key = version + private_key_bytes
    
    # Perform double SHA256
    first_hash = hashlib.sha256(extended_key).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    
    # Add checksum (first 4 bytes of double SHA256)
    final_key = extended_key + second_hash[:4]
    
    # Encode in base58
    return base58.b58encode(final_key).decode('utf-8')

# Get testnet WIF using our custom function
testnet_wif = to_testnet_wif(derived_key.PrivateKey())
print("Private key (Testnet WIF):", testnet_wif)
