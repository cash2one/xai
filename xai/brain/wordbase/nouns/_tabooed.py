

from xai.brain.wordbase.nouns._taboo import _TABOO

#calss header
class _TABOOED(_TABOO, ):
	def __init__(self,): 
		_TABOO.__init__(self)
		self.name = "TABOOED"
		self.specie = 'nouns'
		self.basic = "taboo"
		self.jsondata = {}
