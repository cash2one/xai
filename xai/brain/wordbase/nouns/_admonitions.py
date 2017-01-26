

from xai.brain.wordbase.nouns._admonition import _ADMONITION

#calss header
class _ADMONITIONS(_ADMONITION, ):
	def __init__(self,): 
		_ADMONITION.__init__(self)
		self.name = "ADMONITIONS"
		self.specie = 'nouns'
		self.basic = "admonition"
		self.jsondata = {}
