# Copyright (C) 2018-2024 The python-bitcoin-utils developers
#
# This file is part of python-bitcoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoin-utils, including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.


from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wpkhAddress, P2wshAddress, P2shAddress, PrivateKey
import argparse


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate Bitcoin address from WIF key')
    parser.add_argument('--wif', type=str, required=True, help='WIF private key')
    args = parser.parse_args()

    # always remember to setup the network
    setup("testnet")

    # Instantiate from existing WIF key
    priv = PrivateKey.from_wif(args.wif)

    # compressed is the default
    print("\nPrivate key WIF:", priv.to_wif(compressed=True))

    # get the public key
    pub = priv.get_public_key()

    # compressed is the default
    print("Public key:", pub.to_hex(compressed=True))

    # get address from public key
    address = pub.get_segwit_address()

    # print the address and hash - default is compressed address
    print("Native Address:", address.to_string())
    segwit_hash = address.to_witness_program()
    print("Segwit Hash (witness program):", segwit_hash)
    print("Segwit Version:", address.get_type())

if __name__ == "__main__":
    main()
