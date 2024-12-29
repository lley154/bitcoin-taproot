# Bitcoin Transaction
## Setup
Connect and log into the docker Ubuntu 24.10 Linux container with the user created in [Docker Setup](https://github.com/lley154/docker-setup).

### Download and run a Bitcoin Testnet node
```
$ sudo apt update
$ sudo apt-get install lz4
$ cd /data
$ curl -L -O https://snapshots.publicnode.com/bitcoin-testnet-base.tar.lz4
$ lz4 -dc bitcoin-testnet-base.tar.lz4 | tar xf - -C /data
$ cd ~/.bitcoin
$ ln -s /data/testnet3/

```
Update the bitcoin.conf testnet(test) settings
```
$ nano bitcoin.conf
...
[test]
daemon=1
txindex=1
server=1
rpcuser=test
rpcpassword=test1234
rpcallowip=127.0.0.1
fallbackfee=0.0001
# Disable Tor onion service (default: 1)
listenonion=0
```
Startup ```bitcoind``` and confirm it is sync'd to the Bitcoin testnet.
```
$ bitcoind -testnet debug
Bitcoin Core starting
```
Check that the node is connecting to the bitcoin testnet
```
$ tail -f testnet3/debug.log
...
2024-12-29T15:07:57Z [net] received: headers (162003 bytes) peer=1
2024-12-29T15:07:58Z [net] sending getheaders (101 bytes) peer=1
2024-12-29T15:07:58Z [net] more getheaders (from 000000000e66bc2f4dd31f17a263e06a3a671472994f89d87afa9c41e10396a7) to peer=1
2024-12-29T15:07:58Z [net] received: headers (162003 bytes) peer=1
2024-12-29T15:07:58Z [net] sending getheaders (101 bytes) peer=1
2024-12-29T15:07:58Z [net] more getheaders (from 00000000017e3d14b56b61cc3f21d55a740e88e974393bc1495a657a17a75154) to peer=1
2024-12-29T15:07:58Z Pre-synchronizing blockheaders, height: 136000 (~18.85%)
...
2024-12-29T15:13:19Z [validation] Saw new header hash=0000000033929c568ffb4c1f1f5f26bbab489c7c9ecf16a3243ee7e02d1d5252 height=931897
2024-12-29T15:13:19Z [validation] Saw new header hash=00000000188f38dad689f41991aaf2a9595d69788f24a90085effb15e686ac18 height=931898
2024-12-29T15:13:19Z [validation] Saw new header hash=0000000025f9690dd03896935bdea27c567e77790e3f5bdc8c7eb3586f159885 height=931899
...

```
It may take some time for the node to sync to the network and will need to see the height at the current level as seen in the block explorer.
https://blockstream.info/testnet/
```
$ tail -f testnet3/debug.log
...
2024-12-29T15:28:16Z UpdateTip: new best=0000000000868abb1cf5cf1d8b477e42e2eb0091881912c795abb4fb8f5aa1db height=35553 version=0x00000002 log2_work=51.065646 tx=57727 date='2012-11-07T08:49:16Z' progress=0.000504 cache=6.3MiB(46533txo)
2024-12-29T15:28:16Z [bench]   - Connect postprocess: 1.82ms [14.66s (0.41ms/blk)]
2024-12-29T15:28:16Z [bench] - Connect block: 31.94ms [110.77s (3.12ms/blk)]
2024-12-29T15:28:16Z [validation] Enqueuing BlockConnected: block hash=0000000000868abb1cf5cf1d8b477e42e2eb0091881912c795abb4fb8f5aa1db block height=35553
2024-12-29T15:28:16Z [validation] Enqueuing UpdatedBlockTip: new block hash=0000000000868abb1cf5cf1d8b477e42e2eb0091881912c795abb4fb8f5aa1db fork block hash=0000000000bcf28bcc3f375dea612ab1b589bec0fe76808d3485d4ea7d06ec04 (in IBD=true)
...

$ bitcoin-cli -testnet getblockchaininfo
{
  "chain": "test",
  "blocks": 46170,
  "headers": 3603648,
  "bestblockhash": "0000000001051da4ff6f7842db40bac435332bddc406abedf871d03d6487c7a9",
  "difficulty": 16,
  "time": 1357049999,
  "mediantime": 1357048897,
  "verificationprogress": 0.0006296089201078222,
  "initialblockdownload": true,
  "chainwork": "00000000000000000000000000000000000000000000000000107c1e199b80cf",
  "size_on_disk": 20633734,
  "pruned": false,
  "warnings": ""
}

```

### Setup Python environment 
```
$ cd ~
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
(myenv) $ bitcoin-cli -testnet getblockchaininfo
{
  "chain": "test",
  "blocks": 2231687,
  "headers": 3591118,
  "bestblockhash": "000000000000e1dc72b684468691a821c03adb5e7a5e7cdee7c96c06c2c42c0e",
  "difficulty": 6.335250616269515,
  "time": 1653527384,
  "mediantime": 1653527381,
  "verificationprogress": 0.5496184945503476,
  "initialblockdownload": true,
  "chainwork": "00000000000000000000000000000000000000000000069f7e84745022cf6c2c",
  "size_on_disk": 30917379976,
  "pruned": false,
  "warnings": ""
}

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
(myenv) $ python3 bip39.py 
lawn tide concert sudden obscure wise trouble clown fatigue inject rather boring lab unique siren bundle busy analyst task way razor shine raw subway
Seed (hex): 539848603f05552138c29b1e5898c8097fd1a9426ff2881688b441e70ceccafb4f0af306612e7811ea42a15bd80dfde9f90bba40d4692fa5f974cbc00be01e93

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




