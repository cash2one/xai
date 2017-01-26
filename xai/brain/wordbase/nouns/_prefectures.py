

from xai.brain.wordbase.nouns._prefecture import _PREFECTURE

#calss header
class _PREFECTURES(_PREFECTURE, ):
	def __init__(self,): 
		_PREFECTURE.__init__(self)
		self.name = "PREFECTURES"
		self.specie = 'nouns'
		self.basic = "prefecture"
		self.jsondata = {}
