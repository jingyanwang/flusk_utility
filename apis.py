#########
from flask_restplus import Api
from server_path import ns as ns1
import argsparser
import os, logging.config

args = argsparser.prepare_args()

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

api = Api(
	title='PAX Message Intelligence (PAMI) engine',
	version='1.0.0',
	description='PAX Message Intelligence (PAMI) engine',
)

if args.activate_detection:
	api.add_namespace(ns1)
#########
