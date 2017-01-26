

from xai.brain.wordbase.nouns._conjugation import _CONJUGATION

#calss header
class _CONJUGATIONS(_CONJUGATION, ):
	def __init__(self,): 
		_CONJUGATION.__init__(self)
		self.name = "CONJUGATIONS"
		self.specie = 'nouns'
		self.basic = "conjugation"
		self.jsondata = {}
