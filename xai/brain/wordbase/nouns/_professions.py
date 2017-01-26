

from xai.brain.wordbase.nouns._profession import _PROFESSION

#calss header
class _PROFESSIONS(_PROFESSION, ):
	def __init__(self,): 
		_PROFESSION.__init__(self)
		self.name = "PROFESSIONS"
		self.specie = 'nouns'
		self.basic = "profession"
		self.jsondata = {}
