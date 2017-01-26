

from xai.brain.wordbase.nouns._hospital import _HOSPITAL

#calss header
class _HOSPITALS(_HOSPITAL, ):
	def __init__(self,): 
		_HOSPITAL.__init__(self)
		self.name = "HOSPITALS"
		self.specie = 'nouns'
		self.basic = "hospital"
		self.jsondata = {}
