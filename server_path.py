##############
import time
import logging
import argsparser
from flask_restplus import *
from flask import *

ns = Namespace('pami', description='')
args = argsparser.prepare_args()

parser = ns.parser()
parser.add_argument('text', type=str, location='json')

req_fields = {'text': fields.String(\
	example = u"this is an input text")\
	}
pami_req = ns.model('pami_req', req_fields)

attribute = ns.model('', \
	{'entity': fields.String,\
	'score': fields.Float})

rsp_fields = {\
	'attribute': fields.List(\
	fields.Nested(attribute)),\
	'error':fields.String,\
	'running_time':fields.Float\
	}

pami_rsp = ns.model('pami_rsp', rsp_fields)

@ns.route('/predict')
class pami(Resource):
	def __init__(self, *args, **kwargs):
		super(pami, self).__init__(*args, **kwargs)
	@ns.marshal_with(pami_rsp)
	@ns.expect(pami_req)
	def post(self):
		try:
			start = time.time()
			args = parser.parse_args()			
			output = {}
			output['attribute'] = [{'entity':args['text'],\
						     'score':0.978}]
			output['running_time'] = float(time.time()- start)
			output['error'] = 'success'
			return output, 200
		except Exception as e:
			return {'error': str(e)}
##############
