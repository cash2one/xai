

from xai.brain.wordbase.nouns._hairstylist import _HAIRSTYLIST

#calss header
class _HAIRSTYLISTS(_HAIRSTYLIST, ):
	def __init__(self,): 
		_HAIRSTYLIST.__init__(self)
		self.name = "HAIRSTYLISTS"
		self.specie = 'nouns'
		self.basic = "hairstylist"
		self.jsondata = {}
