

from xai.brain.wordbase.verbs._request import _REQUEST

#calss header
class _REQUESTING(_REQUEST, ):
	def __init__(self,): 
		_REQUEST.__init__(self)
		self.name = "REQUESTING"
		self.specie = 'verbs'
		self.basic = "request"
		self.jsondata = {}
