#!/usr/bin/env python

import subprocess
import sys
import argparse
from os import path

# Default file path
priv_key_path = '/autonity/sec-peers/private_key'
pwd_path = '/autonity/sec-account-pwd/account.pwd'
genesis_path = '/autonity/cm-genesis/genesis.json'
blockchain_path = '/autonity/blockchain/'
keys_path = '/autonity/keys'


def execute(cmd):
    try:
        process = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        print(process.decode())
    except subprocess.CalledProcessError as e:
        sys.exit(e.output.decode())
    return process


def import_account(debug):
    if debug:
        debug = '--debug --verbosity 6'
    else:
        debug = ''
    execute(
        '/usr/local/bin/autonity {0} account import {1} --keystore {2} --password {3}'.format(
            debug,
            priv_key_path,
            keys_path + '/keystore',
            pwd_path
        )
    )
    print('INFO ==== Imported key from secret and created keystore')


def blockchain_init(debug):
    if debug:
        debug = '--debug --verbosity 6'
    else:
        debug = ''
    execute(
        '/usr/local/bin/autonity {0} --datadir {1} --keystore {2} --nodekey {3} init {4}'.format(
            debug,
            blockchain_path,
            keys_path + '/keystore',
            priv_key_path,
            genesis_path
        )
    )
    print('INFO ==== Init new database for blockchain')


def main():
    parser = argparse.ArgumentParser(description='Import private eth key to autonity account. Initialise blockchain')
    parser.add_argument('--debug',
                        dest='debug',
                        type=bool,
                        default=False,
                        help='Enable debug level. (default: %(default)s)'
                        )
    args = parser.parse_args()


    if not path.exists(keys_path + '/keystore'):
        print('INFO ==== Start import private key to autonity account')
        import_account(args.debug)
    else:
        print('INFO ==== Skip autonity account private key import: ' + keys_path + '/keystore is already exist.')
    if not path.exists(blockchain_path + 'autonity'):
        print('INFO ==== Start autonity init step')
        blockchain_init(args.debug)
    else:
        print('INFO ==== Skip autonity init step: ' + blockchain_path + 'autonity is already exist.')
    print('INFO ==== Initial steps completed')


if __name__ == '__main__':
    main()
