

from xai.brain.wordbase.nouns._taboo import _TABOO

#calss header
class _TABOOS(_TABOO, ):
	def __init__(self,): 
		_TABOO.__init__(self)
		self.name = "TABOOS"
		self.specie = 'nouns'
		self.basic = "taboo"
		self.jsondata = {}
