

from xai.brain.wordbase.nouns._radiologist import _RADIOLOGIST

#calss header
class _RADIOLOGISTS(_RADIOLOGIST, ):
	def __init__(self,): 
		_RADIOLOGIST.__init__(self)
		self.name = "RADIOLOGISTS"
		self.specie = 'nouns'
		self.basic = "radiologist"
		self.jsondata = {}
