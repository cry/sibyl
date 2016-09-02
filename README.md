# Sibyl

Takes recovery questions. Generates salt and hashes with sha256 for a unique answer.

By using a global salt instead of UUIDs, only the salt needs to be stored to generate answers for all sites, reducing the risk of lost answers and a simpler program.

## Install

    git clone https://github.com/cry/sibyl .
    chmod +x sibyl
    ln -s sibyl /usr/local/bin/sibyl

## Usage

    sibyl "How many fingers are you missing on your feet?"
    5e35874fea91393122de5cfee1b47f5327918788f902dff51f550ecc8f8f79f0


The MIT License (MIT)
Copyright (c) 2016 Carey Li

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.