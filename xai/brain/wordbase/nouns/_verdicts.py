

from xai.brain.wordbase.nouns._verdict import _VERDICT

#calss header
class _VERDICTS(_VERDICT, ):
	def __init__(self,): 
		_VERDICT.__init__(self)
		self.name = "VERDICTS"
		self.specie = 'nouns'
		self.basic = "verdict"
		self.jsondata = {}
