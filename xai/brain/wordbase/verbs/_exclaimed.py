

from xai.brain.wordbase.verbs._exclaim import _EXCLAIM

#calss header
class _EXCLAIMED(_EXCLAIM, ):
	def __init__(self,): 
		_EXCLAIM.__init__(self)
		self.name = "EXCLAIMED"
		self.specie = 'verbs'
		self.basic = "exclaim"
		self.jsondata = {}
