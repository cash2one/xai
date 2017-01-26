

from xai.brain.wordbase.verbs._appraise import _APPRAISE

#calss header
class _APPRAISED(_APPRAISE, ):
	def __init__(self,): 
		_APPRAISE.__init__(self)
		self.name = "APPRAISED"
		self.specie = 'verbs'
		self.basic = "appraise"
		self.jsondata = {}
