

from xai.brain.wordbase.nouns._parliament import _PARLIAMENT

#calss header
class _PARLIAMENTS(_PARLIAMENT, ):
	def __init__(self,): 
		_PARLIAMENT.__init__(self)
		self.name = "PARLIAMENTS"
		self.specie = 'nouns'
		self.basic = "parliament"
		self.jsondata = {}
