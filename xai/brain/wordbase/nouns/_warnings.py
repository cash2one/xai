

from xai.brain.wordbase.nouns._warning import _WARNING

#calss header
class _WARNINGS(_WARNING, ):
	def __init__(self,): 
		_WARNING.__init__(self)
		self.name = "WARNINGS"
		self.specie = 'nouns'
		self.basic = "warning"
		self.jsondata = {}
