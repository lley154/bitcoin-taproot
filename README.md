# Bitcoin Transaction
## Setup
Connect and log into the docker Ubuntu 24.10 Linux container with the user created in [Docker Setup](https://github.com/lley154/docker-setup).

```
$ sudo apt update
$ sudo apt install python3-pip
$ sudo apt install python3.12-venv
```
Create a virtual python environment
```
$ python3 -m venv myenv
```
Activate the virtual python environment
```
$ source myenv/bin/activate
$ pip install mnemonic
$ pip install bip32utils
$ pip install bitcoin-utils

```
Download repo
```
$ git clone https://github.com/lley154/bitcoin-transaction.git 
$ cd bitcoin-transaction/scripts
```
## Create Bitcoin Addresses
Create a 24 word seed phrase
```
(myenv) $ python3 bip39.py 
Seed phrase: sister object cereal ride sniff yellow virus brief work merry employ flat west arch live curious come magnet advice chalk steel chief grab promote
Seed (hex): 539848603f05552138c29b1e5898c8097fd1a9426ff2881688b441e70ceccafb4f0af306612e7811ea42a15bd80dfde9f90bba40d4692fa5f974cbc00be01e93
```
Create private key in WIF format
```
(myenv) $ python3 private-keys.py –-seed “sister object cereal ride sniff yellow virus brief work merry employ flat west arch live curious come magnet advice chalk steel chief grab promote”
Private key (Testnet WIF): 92MyQw9orqNdTYaeEDRcidKhGyY93gyACjXHdPoCQiryq7pPJWF
```
Create a segwit address using the private key
```
(myenv) $ python3 segwit-address.py --wif 92MyQw9orqNdTYaeEDRcidKhGyY93gyACjXHdPoCQiryq7pPJWF

Private key WIF: cR1Zze1spxWTvAPVKKqeejKWmWYSWsQscnggPdcuMhmbqGXrNQV8
Public key: 032fb631f581add2ba8a1226442812e6bf6147c66abb6eae9855f46e9b6374b580
Native Address: tb1qfyanzs5hprvzyt7mwurmlq9vnz64w9xntgvgzz
Segwit Hash (witness program): 493b31429708d8222fdb7707bf80ac98b55714d3
Segwit Version: p2wpkhv0
```
## Bitcoin Testnet Faucet
Using a Bitcoin testnet faucet, send some funds to the segwit address

https://coinfaucet.eu/en/btc-testnet/

Look at the transaction on a blockchain explorer

https://blockstream.info/testnet/tx/057f1e116b7b12bb1c2b64603ae1152b44baaff75f5722cfa10bd294a1c2cd81

Next, wait for the UTXO to show up in the local bitcoin testnet node
```
(myenv) $ bitcoin-cli -testnet scantxoutset start '["addr(tb1qfyanzs5hprvzyt7mwurmlq9vnz64w9xntgvgzz)"]'
{
  "success": true,
  "txouts": 21448937,
  "height": 1514263,
  "bestblock": "00000000000001e7d62e4d3bc7ebe2b6c14fb55154084257f2be2bb4bbcabb18",
  "unspents": [
  ],
  "total_amount": 0.00000000
}
```
## Transfer Funds
Create another address to send the funds to
```
(myenv) $ python3 private-keys.py --seed "lawn tide concert sudden obscure wise trouble clown fatigue inject rather boring lab unique siren bundle busy analyst task way razor shine raw subway"
Private key (Testnet WIF): 92WB7dwihzbSMSXwP9Rj3SdbFDoox4ZHVpmPQi8dVTYrzzHe7FW

(myenv) $ python3 segwit-address.py --wif 92WB7dwihzbSMSXwP9Rj3SdbFDoox4ZHVpmPQi8dVTYrzzHe7FW

Private key WIF: cRdmeJ4X5wCzuDhZ2kC8Zn8W9mXcE2hVpDpuueYg4cBdgXAQcjLU
Public key: 035bfbbd7cea81f580285c98db3f4e00418448a529af5216bf04bfe7814be6abe7
Native Address: tb1qlqc6f2n6lwvrrcpxn7kg8muwgg4cr9as0lqk0q
Segwit Hash (witness program): f831a4aa7afb9831e0269fac83ef8e422b8197b0
Segwit Version: p2wpkhv0
```
Now transfer the funds to the new address
```
(myenv) python3 $spend_p2wpkh_transaction.py --wif 92MyQw9orqNdTYaeEDRcidKhGyY93gyACjXHdPoCQiryq7pPJWF --utxoId 057f1e116b7b12bb1c2b64603ae1152b44baaff75f5722cfa10bd294a1c2cd81 --utxoIdx 0 --toAddr tb1qlqc6f2n6lwvrrcpxn7kg8muwgg4cr9as0lqk0q

```




