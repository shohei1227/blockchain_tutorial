#! usr/bin/python3
# block.py

import json
import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.dict = {str(i): j for i, j in self.__dict__.items()}
        self.now_hash = self.calc_hash()
 
    
    def calc_hash(self):
        block_string = json.dumps(self.dict, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

