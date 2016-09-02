#!/usr/local/bin/python3

import os
import json
import argparse
import hashlib

from base64 import b64encode

# Arguments

parser = argparse.ArgumentParser(description='Generates unique answers to secret questions.')

parser.add_argument('question', metavar='question', type=str,
                    help='Question to hash')

args = parser.parse_args()

# Sybil main

sybil_home = '%s/.sibyl' % os.path.expanduser("~")
sybil_config = '%s/key' % sybil_home

if not os.path.isfile(sybil_config):
    print('Sibyl keyfile not found, generating...')

    key = b64encode(os.urandom(512)).decode('utf-8')

    print('Your key is %s' % key)

    print('Save your key to a safe place as a backup.')

    os.makedirs(sybil_home)
    open(sybil_config, 'w', encoding='utf-8').write(key)

if 'key' not in globals():
    key = open(sybil_config, 'r', encoding='utf-8').read()

print(hashlib.sha256(("%s%s" % (args.question, key)).encode('utf-8')).hexdigest())