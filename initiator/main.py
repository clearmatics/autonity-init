#!/usr/bin/env python

import subprocess
import sys
from os import listdir

# Default file path
priv_key_path = '/autonity/sec-peers/private_key'
pwd_path = '/autonity/sec-account-pwd/account.pwd'
genesis_path = '/autonity/cm-genesis/genesis.json'
blockchain_path = '/autonity/blockchain/'
keys_path = '/autonity/keys'


def execute(cmd):
    try:
        process = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.output)
    return process


def import_account():
    execute(
        '/usr/local/bin/autonity account import {0} --keystore {1} --password {2}'.format(
            priv_key_path,
            keys_path + '/keystore',
            pwd_path
        )
    )
    print('INFO: Imported key from secret and created keystore')


def blockchain_init():
    execute(
        '/usr/local/bin/autonity --datadir {0} --keystore {1} --nodekey {2} init {3}'.format(
            blockchain_path,
            keys_path + '/keystore',
            priv_key_path,
            genesis_path
        )
    )
    print('INFO: Init new database for blockchain')


def main():
    if not listdir(keys_path):
        import_account()
    if not listdir(blockchain_path):
        blockchain_init()


if __name__ == '__main__':
    main()
