

from xai.brain.wordbase.nouns._province import _PROVINCE

#calss header
class _PROVINCES(_PROVINCE, ):
	def __init__(self,): 
		_PROVINCE.__init__(self)
		self.name = "PROVINCES"
		self.specie = 'nouns'
		self.basic = "province"
		self.jsondata = {}
