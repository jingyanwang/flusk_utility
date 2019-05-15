##############
import logging
import argsparser
from flask_restplus import *
from flask import *

ns = Namespace('', description='pami')
args = argsparser.prepare_args()

parser = ns.parser()
parser.add_argument('text', type=str, location='json')
parser.add_argument('language', type=str, location='json')
parser.add_argument('personal_message', type=str, location='json')
parser.add_argument('name', type=list, location='json')
parser.add_argument('title', type=list, location='json')
parser.add_argument('location', type=list, location='json')
parser.add_argument('time', type=list, location='json')

req_fields = {'text': fields.String(\
	example = u"see you in dubai at 7 pm"),\
	'language':fields.String(example = u"en"),\
	'message_type':fields.String(example = u"personal_message"),\
	'name':fields.List(fields.String, example = []),\
	'title':fields.List(fields.String, example = []),\
	'location':fields.List(fields.String, example = [u"dubai"]),\
	'time':fields.List(fields.String, example = [u"7 pm"])\
	}

meeting_attendee = ns.model('meeting_attendee', \
	{'meeting_attendee': fields.String,\
	'meeting_attendee_score': fields.Float})

meeting_time = ns.model('meeting_time', \
	{'meeting_time': fields.String,\
	'meeting_time_score': fields.Float})

meeting_location = ns.model('meeting_place', \
	{'meeting_location': fields.String,\
	'meeting_location_score': fields.Float})

rsp_fields = {\
	'meeting_attendee': fields.List(\
	fields.Nested(meeting_attendee)),\
	'meeting_time': fields.List(\
	fields.Nested(meeting_time)),\
	'meeting_location': fields.List(\
	fields.Nested(meeting_location)),\
	'running_time':fields.Float
	}

pami_req = ns.model('pami_req', req_fields)
pami_rsp = ns.model('pami_rsp', rsp_fields)

@ns.route('/pami_meeting_detection')
class pami(Resource):
	def __init__(self, *args, **kwargs):
		super(pami, self).__init__(*args, **kwargs)
	@ns.marshal_with(pami_rsp)
	@ns.expect(pami_req)
	def post(self):
		try:
			args = parser.parse_args()
			start = time.time()
			output = {}
			output['running_time'] = float(time.time()- start)
			return output, 200
			output['error'] = 'success'
			return output, 200
		except Exception as e:
			return {'error': str(e)}
##############
