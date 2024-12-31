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
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, TxWitnessInput
from bitcoinutils.keys import P2wpkhAddress, P2pkhAddress, PrivateKey
from bitcoinutils.script import Script
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Spend transaction from WIF key and UTXO')
    parser.add_argument('--wif', type=str, required=True, help='WIF private key')
    parser.add_argument('--utxoId', type=str, required=True, help='UtxoId to spend')
    parser.add_argument('--vout', type=int, required=True, help='vout of utxoId')
    parser.add_argument('--toAddr', type=str, required=True, help='To Address')
    parser.add_argument('--spendAmt', type=float, required=True, help='The amount to spend from a UTXO')
    parser.add_argument('--transferAmt', type=float, required=True, help='The amount to send to an Address')
    args = parser.parse_args()

    # always remember to setup the network
    setup("testnet")

    # Instantiate from existing WIF key
    priv = PrivateKey.from_wif(args.wif)
    pub = priv.get_public_key()

    fromAddress = pub.get_segwit_address()
    print(fromAddress.to_string())

    # amount is needed to sign the segwit input
    fromAddressAmount = to_satoshis(args.spendAmt)

    # UTXO of fromAddress 
    txid = args.utxoId
    vout = args.vout

    # To address from args
    toAddress = P2wpkhAddress(args.toAddr)

    # create transaction input from tx id of UTXO
    txin = TxInput(txid, vout)

    # in segwit the signature message should commit to the script code
    # that corresponds to the segwit transaction output
    # the script code (template) required for signing for p2wpkh is the
    # same as p2pkh
    script_code = Script(
        ["OP_DUP", "OP_HASH160", pub.to_hash160(), "OP_EQUALVERIFY", "OP_CHECKSIG"]
    )

    # create transaction output
    txOut = TxOutput(to_satoshis(args.transferAmt), toAddress.to_script_pub_key())

    # create transaction without change output - if at least a single input is
    # segwit we need to set has_segwit=True
    tx = Transaction([txin], [txOut], has_segwit=True)

    print("\nRaw transaction:\n" + tx.serialize())

    sig = priv.sign_segwit_input(tx, 0, script_code, fromAddressAmount)

    # note that TxWitnessInput gets a list of witness items (not script opcodes)
    tx.witnesses.append(TxWitnessInput([sig, pub.to_hex()]))

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + tx.serialize())
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()
