

from xai.brain.wordbase.verbs._empanel import _EMPANEL

#calss header
class _EMPANELED(_EMPANEL, ):
	def __init__(self,): 
		_EMPANEL.__init__(self)
		self.name = "EMPANELED"
		self.specie = 'verbs'
		self.basic = "empanel"
		self.jsondata = {}
