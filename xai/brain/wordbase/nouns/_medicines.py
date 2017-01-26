

from xai.brain.wordbase.nouns._medicine import _MEDICINE

#calss header
class _MEDICINES(_MEDICINE, ):
	def __init__(self,): 
		_MEDICINE.__init__(self)
		self.name = "MEDICINES"
		self.specie = 'nouns'
		self.basic = "medicine"
		self.jsondata = {}
