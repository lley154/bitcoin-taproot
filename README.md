# Bitcoin Taproot
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
```
Install bitcoin-utils and download repo
```
$ pip install bitcoin-utils
$ git clone https://github.com/lley154/python-bitcoin-utils.git 
$ cd python-bitcoin-utils.git
```
Execute Hierarchical Deterministic Keys python script
```
(myenv) $ python3 hd_keys.py 
Ext. private key: tprv8ZgxMBicQKsPdQR9RuHpGGxSnNq8Jr3X4WnT6Nf2eq7FajuXyBep5KWYpYEixxx5XdTm1Ntpe84f3cVcF7mZZ7mPkntaFXLGJD2tS7YJkWU
Derivation path: m/86'/1'/0'/0/1
WIF: cTLeemg1bCXXuRctid7PygEn7Svxj4zehjTcoayrbEYPsHQo248w
Pubkey: 0271fe85f75e97d22e74c2dd6425e843def8b662b928f24f724ae6a2fd0c4e0419
Legacy address: mtVHHCqCECGwiMbMoZe8ayhJHuTdDbYWdJ
Segwit address: tb1q3ey2d3gs3mavyfknxqvt2drmkf9dasm6nndjgj
Taproot address: tb1pk426x6qvmncj5vzhtp5f2pzhdu4qxsshszswga8ea6sycj9nulmsu7syz0


New derivation path: m/86'/1'/0'/0/5
WIF: cNxX8M7XU8VNa5ofd8yk1eiZxaxNrQQyb7xNpwAmsrzEhcVwtCjs
Pubkey: 03d871a600ada6db6cfe0908f2ef7def22b6205f32a36fa5d78e788ed2e0536b7c
Legacy address: mi2topABG1QdNYijnkdxZ5jNtXmd3b2ZpY
Segwit address: tb1qrwvarkp2036g5q708tzfcy7nu8nx6znahuk5at
Taproot address: tb1p6ssne4tjqlez485s2vpqq7uehpzfz5689x747sr9hh959mgsln2sdpsxdp
Legacy address from mnemonic mz63brMnFrXP4ZF9V75d9VrkKPM5gUyS9H
```

