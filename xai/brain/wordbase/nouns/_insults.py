

from xai.brain.wordbase.nouns._insult import _INSULT

#calss header
class _INSULTS(_INSULT, ):
	def __init__(self,): 
		_INSULT.__init__(self)
		self.name = "INSULTS"
		self.specie = 'nouns'
		self.basic = "insult"
		self.jsondata = {}
