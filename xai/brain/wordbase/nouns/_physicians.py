

from xai.brain.wordbase.nouns._physician import _PHYSICIAN

#calss header
class _PHYSICIANS(_PHYSICIAN, ):
	def __init__(self,): 
		_PHYSICIAN.__init__(self)
		self.name = "PHYSICIANS"
		self.specie = 'nouns'
		self.basic = "physician"
		self.jsondata = {}
