"""
module to import all necessary modules
"""

# tornado modules
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.escape import json_encode, json_decode
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.web import RequestHandler, Application, removeslash

# other modules
import json
from os.path import join, dirname, isfile
from motor import MotorClient
import jwt
from bson.objectid import ObjectId
import os, uuid, sys
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta

secret="gnberghnergb"

db = MotorClient()["iwp"]
