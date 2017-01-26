

from xai.brain.wordbase.nouns._campground import _CAMPGROUND

#calss header
class _CAMPGROUNDS(_CAMPGROUND, ):
	def __init__(self,): 
		_CAMPGROUND.__init__(self)
		self.name = "CAMPGROUNDS"
		self.specie = 'nouns'
		self.basic = "campground"
		self.jsondata = {}
