

from xai.brain.wordbase.verbs._download import _DOWNLOAD

#calss header
class _DOWNLOADED(_DOWNLOAD, ):
	def __init__(self,): 
		_DOWNLOAD.__init__(self)
		self.name = "DOWNLOADED"
		self.specie = 'verbs'
		self.basic = "download"
		self.jsondata = {}
