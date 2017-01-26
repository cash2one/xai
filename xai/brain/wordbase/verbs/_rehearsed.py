

from xai.brain.wordbase.verbs._rehearse import _REHEARSE

#calss header
class _REHEARSED(_REHEARSE, ):
	def __init__(self,): 
		_REHEARSE.__init__(self)
		self.name = "REHEARSED"
		self.specie = 'verbs'
		self.basic = "rehearse"
		self.jsondata = {}
