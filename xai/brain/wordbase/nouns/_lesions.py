

from xai.brain.wordbase.nouns._lesion import _LESION

#calss header
class _LESIONS(_LESION, ):
	def __init__(self,): 
		_LESION.__init__(self)
		self.name = "LESIONS"
		self.specie = 'nouns'
		self.basic = "lesion"
		self.jsondata = {}
