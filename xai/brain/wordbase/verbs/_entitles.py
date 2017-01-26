

from xai.brain.wordbase.verbs._entitle import _ENTITLE

#calss header
class _ENTITLES(_ENTITLE, ):
	def __init__(self,): 
		_ENTITLE.__init__(self)
		self.name = "ENTITLES"
		self.specie = 'verbs'
		self.basic = "entitle"
		self.jsondata = {}
