##############server_path.py##############

import time
import logging
import argsparser
from flask_restx import *
from flask import *

ns = Namespace(
	'my_space', 
	description='machine learning as a service',
	)

args = argsparser.prepare_args()

#############

chunking_parser = ns.parser()
chunking_parser.add_argument('text', type=str, location='json')

chunking_inputs = ns.model(
	'my_space', 
		{
			'text': fields.String(example = u"this is an input text")
		}
	)

@ns.route('/chunking')
class chunking_api(Resource):
	def __init__(self, *args, **kwargs):
		super(chunking_api, self).__init__(*args, **kwargs)
	@ns.expect(chunking_inputs)
	def post(self):		
		start = time.time()
		try:			
			args = chunking_parser.parse_args()		
			output = {}
			output['chunks'] = [
				'chunck1',  
				'chunck2',
			]
			output['status'] = 'success'
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['status'] = str(e)
			output['running_time'] = float(time.time()- start)
			return output

#############

extraction_parser = ns.parser()
extraction_parser.add_argument('chunk', type=str, location='json')

extraction_inputs = ns.model(
	'my_space', 
		{
			'chunk': fields.String(example = u"this is a chunk")
		}
	)

@ns.route('/extraction')
class extraction_api(Resource):
	def __init__(self, *args, **kwargs):
		super(extraction_api, self).__init__(*args, **kwargs)
	@ns.expect(extraction_inputs)
	def post(self):		
		start = time.time()
		try:			
			args = extraction_parser.parse_args()		
			output = {}
			output['entities'] = [
				{'text':'entity1','score':0.97},
				{'text':'entity2','score':0.91},
			]
			output['status'] = 'success'
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['status'] = str(e)
			output['running_time'] = float(time.time()- start)
			return output

##############server_path.py##############