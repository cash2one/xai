

from xai.brain.wordbase.verbs._outlive import _OUTLIVE

#calss header
class _OUTLIVED(_OUTLIVE, ):
	def __init__(self,): 
		_OUTLIVE.__init__(self)
		self.name = "OUTLIVED"
		self.specie = 'verbs'
		self.basic = "outlive"
		self.jsondata = {}
