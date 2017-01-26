

from xai.brain.wordbase.nouns._sarcasm import _SARCASM

#calss header
class _SARCASMS(_SARCASM, ):
	def __init__(self,): 
		_SARCASM.__init__(self)
		self.name = "SARCASMS"
		self.specie = 'nouns'
		self.basic = "sarcasm"
		self.jsondata = {}
