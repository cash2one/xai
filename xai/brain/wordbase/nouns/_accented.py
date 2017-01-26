

from xai.brain.wordbase.nouns._accent import _ACCENT

#calss header
class _ACCENTED(_ACCENT, ):
	def __init__(self,): 
		_ACCENT.__init__(self)
		self.name = "ACCENTED"
		self.specie = 'nouns'
		self.basic = "accent"
		self.jsondata = {}
