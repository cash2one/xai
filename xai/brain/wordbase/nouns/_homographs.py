

from xai.brain.wordbase.nouns._homograph import _HOMOGRAPH

#calss header
class _HOMOGRAPHS(_HOMOGRAPH, ):
	def __init__(self,): 
		_HOMOGRAPH.__init__(self)
		self.name = "HOMOGRAPHS"
		self.specie = 'nouns'
		self.basic = "homograph"
		self.jsondata = {}
