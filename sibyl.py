#!/usr/local/bin/python3

import os
import json
import argparse
import hashlib

from base64 import b64encode

# Arguments

parser = argparse.ArgumentParser(description='Generates unique answers to secret questions using a global salt.')

parser.add_argument('question', metavar='question', type=str,
                    help='Question to hash')

args = parser.parse_args()

# Sibyl main

sibyl_home = '%s/.sibyl' % os.path.expanduser("~")
sibyl_config = '%s/key' % sibyl_home

if not os.path.isfile(sibyl_config):
    print('Sibyl keyfile not found, generating...')

    key = b64encode(os.urandom(512)).decode('utf-8')

    print('Your key is %s' % key)

    print('Save your key to a safe place as a backup.')

    os.makedirs(sibyl_home)
    open(sibyl_config, 'w', encoding='utf-8').write(key)

if 'key' not in globals():
    key = open(sibyl_config, 'r', encoding='utf-8').read()

print(hashlib.sha256(("%s%s" % (args.question, key)).encode('utf-8')).hexdigest())
