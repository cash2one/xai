

from xai.brain.wordbase.nouns._silent import _SILENT

#calss header
class _SILENTER(_SILENT, ):
	def __init__(self,): 
		_SILENT.__init__(self)
		self.name = "SILENTER"
		self.specie = 'nouns'
		self.basic = "silent"
		self.jsondata = {}
