

from xai.brain.wordbase.verbs._print import _PRINT

#calss header
class _PRINTS(_PRINT, ):
	def __init__(self,): 
		_PRINT.__init__(self)
		self.name = "PRINTS"
		self.specie = 'verbs'
		self.basic = "print"
		self.jsondata = {}
