

from xai.brain.wordbase.nouns._comma import _COMMA

#calss header
class _COMMAS(_COMMA, ):
	def __init__(self,): 
		_COMMA.__init__(self)
		self.name = "COMMAS"
		self.specie = 'nouns'
		self.basic = "comma"
		self.jsondata = {}
