

from xai.brain.wordbase.nouns._stamp import _STAMP

#calss header
class _STAMPED(_STAMP, ):
	def __init__(self,): 
		_STAMP.__init__(self)
		self.name = "STAMPED"
		self.specie = 'nouns'
		self.basic = "stamp"
		self.jsondata = {}
