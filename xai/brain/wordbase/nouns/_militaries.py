

from xai.brain.wordbase.nouns._military import _MILITARY

#calss header
class _MILITARIES(_MILITARY, ):
	def __init__(self,): 
		_MILITARY.__init__(self)
		self.name = "MILITARIES"
		self.specie = 'nouns'
		self.basic = "military"
		self.jsondata = {}
