#!/usr/bin/env python

import argparse


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


if __name__ == '__main__':
    main()
