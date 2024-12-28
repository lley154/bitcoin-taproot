from mnemonic import Mnemonic
import binascii

# Generate a new seed phrase
mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)  # 24 words
seed = mnemo.to_seed(words)

print("Seed phrase:", words)
print("Seed (hex):", binascii.hexlify(seed).decode())
