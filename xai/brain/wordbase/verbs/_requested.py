

from xai.brain.wordbase.verbs._request import _REQUEST

#calss header
class _REQUESTED(_REQUEST, ):
	def __init__(self,): 
		_REQUEST.__init__(self)
		self.name = "REQUESTED"
		self.specie = 'verbs'
		self.basic = "request"
		self.jsondata = {}
