# Bitcoin Transaction
## Setup
Connect and log into the docker Ubuntu 24.10 Linux container with the user created in [Docker Setup](https://github.com/lley154/docker-setup).

### Download and run a Bitcoin Testnet node
On the Host machine (not the docker instance)
```
$ sudo apt update
$ sudo apt-get install lz4
$ cd /home/your-username/docker-data
$ curl -L -O https://snapshots.publicnode.com/bitcoin-testnet-base.tar.lz4
$ curl -L -O https://snapshots.publicnode.com/bitcoin-testnet-part-3603026.tar.lz4
$ lz4 -dc bitcoin-testnet-base.tar.lz4 | tar xf - -C .
$ lz4 -dc bitcoin-testnet-part-3603026.tar.lz4 | tar xf - -C .
```
Log into the docker container, go to the .bitcoin directory, and create a symbolic link to the external /data directory containing the Bitcoin Testnet blockchain data.
```
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
$ bitcoind -testnet
Bitcoin Core starting
```
Check that the node is connecting to the bitcoin testnet
```
$ tail -f testnet3/debug.log 
2024-12-29T20:07:08Z * Using 2.0 MiB for block index database
2024-12-29T20:07:08Z * Using 56.0 MiB for transaction index database
2024-12-29T20:07:08Z * Using 8.0 MiB for chain state database
2024-12-29T20:07:08Z * Using 384.0 MiB for in-memory UTXO set (plus up to 286.1 MiB of unused mempool space)
2024-12-29T20:07:08Z init message: Loading block index…
2024-12-29T20:07:08Z Assuming ancestors of block 000000000001323071f38f21ea5aae529ece491eadaccce506a59bcc2d968917 have valid signatures.
2024-12-29T20:07:08Z Setting nMinimumChainWork=000000000000000000000000000000000000000000000c59b14e264ba6c15db9
2024-12-29T20:07:08Z Opening LevelDB in /home/lawrence/.bitcoin/testnet3/blocks/index
2024-12-29T20:07:08Z Opened LevelDB successfully
2024-12-29T20:07:08Z Using obfuscation key for /home/lawrence/.bitcoin/testnet3/blocks/index: 0000000000000000

2024-12-29T20:07:36Z LoadBlockIndexDB: last block file = 1091
2024-12-29T20:07:36Z LoadBlockIndexDB: last block file info: CBlockFileInfo(blocks=24, size=15129299, heights=3603003...3603026, time=2024-12-29...2024-12-29)
2024-12-29T20:07:36Z Checking all blk files are present...
2024-12-29T20:07:44Z Initializing chainstate Chainstate [ibd] @ height -1 (null)
2024-12-29T20:07:44Z Opening LevelDB in /home/lawrence/.bitcoin/testnet3/chainstate
2024-12-29T20:07:45Z Opened LevelDB successfully
2024-12-29T20:07:45Z Using obfuscation key for /home/lawrence/.bitcoin/testnet3/chainstate: a561a8ba84e35414
2024-12-29T20:07:47Z Loaded best chain: hashBestChain=00000000000001bd7abacc15392cbb2e23cb9c7c5b26cc82207204b2893b8a8a height=3603026 date=2024-12-29T05:57:24Z progress=0.999815
2024-12-29T20:07:47Z Opening LevelDB in /home/lawrence/.bitcoin/testnet3/chainstate
2024-12-29T20:07:47Z Opened LevelDB successfully
2024-12-29T20:07:47Z Using obfuscation key for /home/lawrence/.bitcoin/testnet3/chainstate: a561a8ba84e35414
2024-12-29T20:07:47Z [Chainstate [ibd] @ height 3603026 (00000000000001bd7abacc15392cbb2e23cb9c7c5b26cc82207204b2893b8a8a)] resized coinsdb cache to 8.0 MiB
2024-12-29T20:07:47Z [Chainstate [ibd] @ height 3603026 (00000000000001bd7abacc15392cbb2e23cb9c7c5b26cc82207204b2893b8a8a)] resized coinstip cache to 384.0 MiB
2024-12-29T20:07:47Z init message: Verifying blocks…
2024-12-29T20:07:47Z Verifying last 6 blocks at level 3
2024-12-29T20:07:47Z Verification progress: 0%
2024-12-29T20:07:53Z Verification progress: 16%
2024-12-29T20:08:02Z Verification progress: 33%
...
2024-12-29T20:08:14Z Verification progress: 99%
2024-12-29T20:08:14Z Verification: No coin database inconsistencies in last 6 blocks (8045 transactions)
2024-12-29T20:08:14Z  block index           65576ms
2024-12-29T20:08:14Z Opening LevelDB in /home/lawrence/.bitcoin/testnet3/indexes/txindex
2024-12-29T20:08:14Z Opened LevelDB successfully
2024-12-29T20:08:14Z Using obfuscation key for /home/lawrence/.bitcoin/testnet3/indexes/txindex: 0000000000000000
2024-12-29T20:08:14Z Setting NODE_NETWORK on non-prune mode
2024-12-29T20:08:14Z block tree size = 3659403
2024-12-29T20:08:14Z nBestHeight = 3603026
2024-12-29T20:08:14Z initload thread start
2024-12-29T20:08:14Z txindex thread start
2024-12-29T20:08:14Z txindex is enabled at height 3603026
2024-12-29T20:08:14Z txindex thread exit
2024-12-29T20:08:14Z Loading 0 mempool transactions from disk...
2024-12-29T20:08:14Z Imported mempool transactions from disk: 0 succeeded, 0 failed, 0 expired, 0 already there, 0 waiting for initial broadcast
2024-12-29T20:08:14Z Bound to 127.0.0.1:18334
2024-12-29T20:08:14Z initload thread exit
2024-12-29T20:08:14Z Bound to [::]:18333
2024-12-29T20:08:14Z Bound to 0.0.0.0:18333
2024-12-29T20:08:14Z Loaded 2 addresses from "anchors.dat"
2024-12-29T20:08:14Z 2 block-relay-only anchors will be tried for connections.
2024-12-29T20:08:14Z init message: Starting network threads…
2024-12-29T20:08:14Z dnsseed thread start
2024-12-29T20:08:14Z opencon thread start
2024-12-29T20:08:14Z msghand thread start
2024-12-29T20:08:14Z init message: Done loading
2024-12-29T20:08:14Z Waiting 300 seconds before querying DNS seeds.
2024-12-29T20:08:14Z addcon thread start
2024-12-29T20:08:14Z net thread start
2024-12-29T20:08:15Z New block-relay-only v1 peer connected: version: 70016, blocks=3603850, peer=0
2024-12-29T20:08:15Z Leaving InitialBlockDownload (latching to false)
2024-12-29T20:08:15Z Saw new header hash=000000000105cb80e8c42db51d0afeb0d043934207ec14f4c4002bc11f4d2da5 height=3603027
2024-12-29T20:08:15Z Saw new header hash=00000000000002173858f78ba4f64afde7137fde0414d31a5fdf1444e4d0c7f6 height=3603028
```

It may take some time for the node to sync to the network and you can see the height at the current level as seen in the block explorer.

https://blockstream.info/testnet/
```
$ bitcoin-cli -testnet getblockchaininfo
{
  "chain": "test",
  "blocks": 3603194,
  "headers": 3603850,
  "bestblockhash": "00000000000001108ceff0f77f85b23e2223e6067c1a132e18879fa78adccfe6",
  "difficulty": 4027453.665054945,
  "time": 1735459086,
  "mediantime": 1735459086,
  "verificationprogress": 0.9998396507242174,
  "initialblockdownload": false,
  "chainwork": "0000000000000000000000000000000000000000000013ac9da9f913fca12013",
  "size_on_disk": 162303438011,
  "pruned": false,
  "warnings": "Unknown new rules activated (versionbit 28)"
}

```

### Setup Python environment in the Docker container
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
(myenv) $ python3 private-keys.py --seed "sister object cereal ride sniff yellow virus brief work merry employ flat west arch live curious come magnet advice chalk steel chief grab promote"
Private key (Testnet WIF): 92JytEnWR9xw9Mi3dbVEK9cvTY16vT1jiZhhy6UyYA39q7QaozE
```
Create a segwit address using the private key
```
(myenv) $ python3 segwit-address.py --wif 92JytEnWR9xw9Mi3dbVEK9cvTY16vT1jiZhhy6UyYA39q7QaozE

Private key WIF: cQnN59qrqcZsytQAcXDbm73Yx7qT8upFYTLfpbCUYWtVxtxmM6JD
Public key: 03b4336f5bc409abeab5290dccf717fdf701a1f6bd5a1fb4504cb59d31c05216fe
Native Address: tb1qr9uq0u3rzd3ce7y956z7q4qkyqkzrz8sytwvmq
Segwit Hash (witness program): 197807f22313638cf885a685e05416202c2188f0
Segwit Version: p2wpkhv0
```
## Bitcoin Testnet Faucet
Using a Bitcoin testnet faucet, send some funds to the segwit address tb1qr9uq0u3rzd3ce7y956z7q4qkyqkzrz8sytwvmq

https://coinfaucet.eu/en/btc-testnet/

Look at the transaction on a blockchain explorer

![image](https://github.com/user-attachments/assets/4d42ef46-0312-4267-a5d1-c026a8653d81)

https://blockstream.info/testnet/tx/9c352a6417712545a22b3686ecb32b01786093309e93d15af6c3f5f12d8ed776 

Next, wait for the block to show up in the local bitcoin testnet node

```
(myenv) $ bitcoin-cli -testnet getblockchaininfo
{
  "chain": "test",
  "blocks": 3603891,
  "headers": 3603891,
  "bestblockhash": "0000000002e43fa5cc84808b469822db1887024a93823a9f8438b9eacdb0192a",
  "difficulty": 1,
  "time": 1735513241,
  "mediantime": 1735512040,
  "verificationprogress": 1,
  "initialblockdownload": false,
  "chainwork": "0000000000000000000000000000000000000000000013ad042b437e4187d932",
  "size_on_disk": 162766141959,
  "pruned": false,
  "warnings": "Unknown new rules activated (versionbit 28)"
}

(myenv) $ bitcoin-cli -testnet scantxoutset start '["addr(tb1qr9uq0u3rzd3ce7y956z7q4qkyqkzrz8sytwvmq)"]'
{
  "success": true,
  "txouts": 186043158,
  "height": 3603891,
  "bestblock": "0000000002e43fa5cc84808b469822db1887024a93823a9f8438b9eacdb0192a",
  "unspents": [
    {
      "txid": "9c352a6417712545a22b3686ecb32b01786093309e93d15af6c3f5f12d8ed776",
      "vout": 1,
      "scriptPubKey": "0014197807f22313638cf885a685e05416202c2188f0",
      "desc": "addr(tb1qr9uq0u3rzd3ce7y956z7q4qkyqkzrz8sytwvmq)#ldvchfv6",
      "amount": 0.00015529,
      "coinbase": false,
      "height": 3603664
    }
  ],
  "total_amount": 0.00015529
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

Create the transaction to transfer the funds to the new address.
```
(myenv) $ python3 spend_p2wpkh_transaction.py --wif 92JytEnWR9xw9Mi3dbVEK9cvTY16vT1jiZhhy6UyYA39q7QaozE --utxoId 9c352a6417712545a22b3686ecb32b01786093309e93d15af6c3f5f12d8ed776 --vout 1 --toAddr tb1qlqc6f2n6lwvrrcpxn7kg8muwgg4cr9as0lqk0q --spendAmt 0.00015529 --transferAmt 0.00010000
tb1qr9uq0u3rzd3ce7y956z7q4qkyqkzrz8sytwvmq

Raw transaction:
0200000000010176d78e2df1f5c3f65ad1939e30936078012bb3ec86362ba245257117642a359c0100000000ffffffff011027000000000000160014f831a4aa7afb9831e0269fac83ef8e422b8197b000000000

Raw signed transaction:
0200000000010176d78e2df1f5c3f65ad1939e30936078012bb3ec86362ba245257117642a359c0100000000ffffffff011027000000000000160014f831a4aa7afb9831e0269fac83ef8e422b8197b00247304402200ea6e38ec6760e5dae1811af386fa44e550060b8aed0b02af2f0e755354e172f02200306df47154cd00f2ee974bd049d303e3d3304c0ef5453c5b7d0efdcca4b163f012103b4336f5bc409abeab5290dccf717fdf701a1f6bd5a1fb4504cb59d31c05216fe00000000

TxId: 87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab
(myenv) lawrence@80e3b38f7216:~/bitcoin-transaction/scripts$ 
```
Test that the transaction is valid.
```
(myenv) $ bitcoin-cli -testnet testmempoolaccept '["0200000000010176d78e2df1f5c3f65ad1939e30936078012bb3ec86362ba245257117642a359c0100000000ffffffff011027000000000000160014f831a4aa7afb9831e0269fac83ef8e422b8197b00247304402200ea6e38ec6760e5dae1811af386fa44e550060b8aed0b02af2f0e755354e172f02200306df47154cd00f2ee974bd049d303e3d3304c0ef5453c5b7d0efdcca4b163f012103b4336f5bc409abeab5290dccf717fdf701a1f6bd5a1fb4504cb59d31c05216fe00000000"]'
[
  {
    "txid": "87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab",
    "wtxid": "8bc0475047c378a64d0bb6ca628ea5a8f83b3693fe4319635221af3c7eae4d57",
    "allowed": true,
    "vsize": 110,
    "fees": {
      "base": 0.00005529,
      "effective-feerate": 0.00050263,
      "effective-includes": [
        "8bc0475047c378a64d0bb6ca628ea5a8f83b3693fe4319635221af3c7eae4d57"
      ]
    }
  }
]
```
Check that there are enough network connections to broadcast the transaction.
```
(myenv)$ bitcoin-cli -testnet getnetworkinfo
{
  "version": 270000,
  "subversion": "/Satoshi:27.0.0/",
  "protocolversion": 70016,
  "localservices": "0000000000000c09",
  "localservicesnames": [
    "NETWORK",
    "WITNESS",
    "NETWORK_LIMITED",
    "P2P_V2"
  ],
  "localrelay": true,
  "timeoffset": 0,
  "networkactive": true,
  "connections": 17,
  "connections_in": 7,
  "connections_out": 10,
  "networks": [
    {
      "name": "ipv4",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "ipv6",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "onion",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "i2p",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "cjdns",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    }
  ],
  "relayfee": 0.00001000,
  "incrementalfee": 0.00001000,
  "localaddresses": [
  ],
  "warnings": "Unknown new rules activated (versionbit 28)"
}

(myenv) $ bitcoin-cli -testnet sendrawtransaction "0200000000010176d78e2df1f5c3f65ad1939e30936078012bb3ec86362ba245257117642a359c0100000000ffffffff011027000000000000160014f831a4aa7afb9831e0269fac83ef8e422b8197b00247304402200ea6e38ec6760e5dae1811af386fa44e550060b8aed0b02af2f0e755354e172f02200306df47154cd00f2ee974bd049d303e3d3304c0ef5453c5b7d0efdcca4b163f012103b4336f5bc409abeab5290dccf717fdf701a1f6bd5a1fb4504cb59d31c05216fe00000000"
87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab

$ bitcoin-cli -testnet getmempoolinfo
{
  "loaded": true,
  "size": 49487,
  "bytes": 14022714,
  "usage": 61805552,
  "total_fee": 34.33665170,
  "maxmempool": 300000000,
  "mempoolminfee": 0.00001000,
  "minrelaytxfee": 0.00001000,
  "incrementalrelayfee": 0.00001000,
  "unbroadcastcount": 0,
  "fullrbf": false
}

$ bitcoin-cli -testnet getmempoolentry 87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab 
{
  "vsize": 110,
  "weight": 437,
  "time": 1735526512,
  "height": 3604138,
  "descendantcount": 1,
  "descendantsize": 110,
  "ancestorcount": 1,
  "ancestorsize": 110,
  "wtxid": "8bc0475047c378a64d0bb6ca628ea5a8f83b3693fe4319635221af3c7eae4d57",
  "fees": {
    "base": 0.00005529,
    "modified": 0.00005529,
    "ancestor": 0.00005529,
    "descendant": 0.00005529
  },
  "depends": [
  ],
  "spentby": [
  ],
  "bip125-replaceable": false,
  "unbroadcast": false
}

$ bitcoin-cli -testnet getrawtransaction 87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab true
{
  "txid": "87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab",
  "hash": "8bc0475047c378a64d0bb6ca628ea5a8f83b3693fe4319635221af3c7eae4d57",
  "version": 2,
  "size": 191,
  "vsize": 110,
  "weight": 437,
  "locktime": 0,
  "vin": [
    {
      "txid": "9c352a6417712545a22b3686ecb32b01786093309e93d15af6c3f5f12d8ed776",
      "vout": 1,
      "scriptSig": {
        "asm": "",
        "hex": ""
      },
      "txinwitness": [
        "304402200ea6e38ec6760e5dae1811af386fa44e550060b8aed0b02af2f0e755354e172f02200306df47154cd00f2ee974bd049d303e3d3304c0ef5453c5b7d0efdcca4b163f01",
        "03b4336f5bc409abeab5290dccf717fdf701a1f6bd5a1fb4504cb59d31c05216fe"
      ],
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 0.00010000,
      "n": 0,
      "scriptPubKey": {
        "asm": "0 f831a4aa7afb9831e0269fac83ef8e422b8197b0",
        "desc": "addr(tb1qlqc6f2n6lwvrrcpxn7kg8muwgg4cr9as0lqk0q)#dsw0hqrh",
        "hex": "0014f831a4aa7afb9831e0269fac83ef8e422b8197b0",
        "address": "tb1qlqc6f2n6lwvrrcpxn7kg8muwgg4cr9as0lqk0q",
        "type": "witness_v0_keyhash"
      }
    }
  ],
  "hex": "0200000000010176d78e2df1f5c3f65ad1939e30936078012bb3ec86362ba245257117642a359c0100000000ffffffff011027000000000000160014f831a4aa7afb9831e0269fac83ef8e422b8197b00247304402200ea6e38ec6760e5dae1811af386fa44e550060b8aed0b02af2f0e755354e172f02200306df47154cd00f2ee974bd049d303e3d3304c0ef5453c5b7d0efdcca4b163f012103b4336f5bc409abeab5290dccf717fdf701a1f6bd5a1fb4504cb59d31c05216fe00000000"
}
```
Finally, check that the transaction can be found in a blockchain explorer
```
https://blockstream.info/testnet/tx/87c482200fe3536af53072405ffd082f2cb56f72ab1444d34147916643a7b9ab

```






