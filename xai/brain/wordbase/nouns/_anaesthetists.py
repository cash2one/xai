

from xai.brain.wordbase.nouns._anaesthetist import _ANAESTHETIST

#calss header
class _ANAESTHETISTS(_ANAESTHETIST, ):
	def __init__(self,): 
		_ANAESTHETIST.__init__(self)
		self.name = "ANAESTHETISTS"
		self.specie = 'nouns'
		self.basic = "anaesthetist"
		self.jsondata = {}
