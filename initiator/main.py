#!/usr/bin/env python

import argparse
import subprocess
import sys
from web3.auto import w3
from os import listdir

# Default file path
priv_key_path = '/autonity/sec-validators/private_key'
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


def generate_node_key():
    print('INFO: Generate node.key from keystore')
    keystores_dir = keys_path + "/keystore"
    keystore_file_path = keystores_dir + "/" + listdir(keystores_dir)[0]
    with open(pwd_path) as pwd_file:
        pwd = pwd_file.read()
        print(pwd)
    with open(keystore_file_path) as keyfile:
        encrypted_key = keyfile.read()
        print(encrypted_key)
        account_private_key = w3.eth.account.decrypt(encrypted_key, "123").hex()[2:]
        print(account_private_key)
    with open(priv_key_path) as priv_key_file:
        print(priv_key_file.read())


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
    parser = argparse.ArgumentParser(description='Prepare pod with autonity for launch')
    parser.add_argument('-type',
                        dest='peer_type',
                        default='observer',
                        choices=['observer', 'validator'],
                        help='Type of peer. For validators will be generated node.key (default: %(default)s)'
                        )
    args = parser.parse_args()
    print(args.peer_type)

    if not listdir(keys_path):
        import_account()
        #generate_node_key()
    if not listdir(blockchain_path):
        blockchain_init()


if __name__ == '__main__':
    main()
