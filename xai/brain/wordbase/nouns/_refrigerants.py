

from xai.brain.wordbase.nouns._refrigerant import _REFRIGERANT

#calss header
class _REFRIGERANTS(_REFRIGERANT, ):
	def __init__(self,): 
		_REFRIGERANT.__init__(self)
		self.name = "REFRIGERANTS"
		self.specie = 'nouns'
		self.basic = "refrigerant"
		self.jsondata = {}
