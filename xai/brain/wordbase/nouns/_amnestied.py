

from xai.brain.wordbase.nouns._amnesty import _AMNESTY

#calss header
class _AMNESTIED(_AMNESTY, ):
	def __init__(self,): 
		_AMNESTY.__init__(self)
		self.name = "AMNESTIED"
		self.specie = 'nouns'
		self.basic = "amnesty"
		self.jsondata = {}
