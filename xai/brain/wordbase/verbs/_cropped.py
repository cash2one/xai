

from xai.brain.wordbase.verbs._crop import _CROP

#calss header
class _CROPPED(_CROP, ):
	def __init__(self,): 
		_CROP.__init__(self)
		self.name = "CROPPED"
		self.specie = 'verbs'
		self.basic = "crop"
		self.jsondata = {}
