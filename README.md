# Sibyl

Takes recovery questions. Generates salt and hashes with sha256 for a unique answer.

By using a global salt instead of UUIDs, only the salt needs to be stored to generate answers for all sites, reducing the risk of lost answers and a simpler program.

## Install

    cd /opt
    mkdir sibyl && cd sibyl
    git clone https://github.com/cry/sibyl .
    chmod +x sibyl.py
    ln -s sibyl.py /usr/local/bin/sibyl

## Usage

    sibyl "How many fingers are you missing on your feet?"
    5e35874fea91393122de5cfee1b47f5327918788f902dff51f550ecc8f8f79f0