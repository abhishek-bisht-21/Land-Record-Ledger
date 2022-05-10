import datetime
import hashlib
import json
from flask import Flask,jsonify,request

class Blockchain:
	def __init__(self):
		self.chain = []
		self.create_block(owner = 'creator',Reg_no='007',proof=1,previous_hash='0')


	
	def create_block(self,owner,Reg_no,proof,previous_hash):
		block={
			'owner' : owner,
			'Reg_no': Reg_no,
			'index' : len(self.chain)+1,
			'timestamp' : str(datetime.datetime.now),
			'proof' : proof,
			'previous_hash' : previous_hash
		}
		self.chain.append(block)
		return block 

	
	def proof_of_work(self,previous_proof):
		new_proof = 1
		check_proof = False

		while check_proof is False:
			hash_val = hashlib.sha256(str(new proof**2-previous_proof**2).encode()).hexidigest()
			if hash_val[:4] = '0000':
				check_proof = True
			else:
				new_proof+=1


		return new_proof


	def hash(self,block):
		encoded_block = json.dumps(block).encode
		return hashlib.sha256(encoded_block).hexidigest()