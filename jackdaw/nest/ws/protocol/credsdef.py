import json

from jackdaw.utils.encoder import UniversalEncoder 
from jackdaw.nest.ws.protocol.cmdtypes import NestOpCmd

class NestOpCredsDef:
	def __init__(self):
		self.adid = None
		self.sid = None
		self.authtype = None
	
	def to_dict(self):
		return self.__dict__
	
	def to_json(self):
		return json.dumps(self.to_dict(), cls = UniversalEncoder)

	@staticmethod
	def from_dict(d):
		print(d)
		cmd = NestOpCredsDef()
		cmd.adid = d['adid']
		cmd.sid = d['sid']
		cmd.authtype = d['authtype']
		return cmd
			
	@staticmethod
	def from_json(jd):
		return NestOpCredsDef.from_dict(json.loads(jd))

	def __repr__(self):
		return 'NestOpCredsDef: adid: %s sid: %s authtype: %s' % (self.adid, self.sid, self.authtype)