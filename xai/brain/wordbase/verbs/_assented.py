

from xai.brain.wordbase.verbs._assent import _ASSENT

#calss header
class _ASSENTED(_ASSENT, ):
	def __init__(self,): 
		_ASSENT.__init__(self)
		self.name = "ASSENTED"
		self.specie = 'verbs'
		self.basic = "assent"
		self.jsondata = {}
