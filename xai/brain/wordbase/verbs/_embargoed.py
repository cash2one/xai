

from xai.brain.wordbase.verbs._embargo import _EMBARGO

#calss header
class _EMBARGOED(_EMBARGO, ):
	def __init__(self,): 
		_EMBARGO.__init__(self)
		self.name = "EMBARGOED"
		self.specie = 'verbs'
		self.basic = "embargo"
		self.jsondata = {}
