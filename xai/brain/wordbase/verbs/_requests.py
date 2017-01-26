

from xai.brain.wordbase.verbs._request import _REQUEST

#calss header
class _REQUESTS(_REQUEST, ):
	def __init__(self,): 
		_REQUEST.__init__(self)
		self.name = "REQUESTS"
		self.specie = 'verbs'
		self.basic = "request"
		self.jsondata = {}
