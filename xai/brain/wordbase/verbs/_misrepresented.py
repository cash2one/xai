

from xai.brain.wordbase.verbs._misrepresent import _MISREPRESENT

#calss header
class _MISREPRESENTED(_MISREPRESENT, ):
	def __init__(self,): 
		_MISREPRESENT.__init__(self)
		self.name = "MISREPRESENTED"
		self.specie = 'verbs'
		self.basic = "misrepresent"
		self.jsondata = {}
