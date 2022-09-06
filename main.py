#! /usr/bin/python3
# main.py
from block import block

def main():
    blockchain = []
    b = block.Block(0, 0, 0, '-')
    print(b)
    blockchain.append(b)
    print(blockchain)


if __name__ == "__main__":
    main() 