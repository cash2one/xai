

from xai.brain.wordbase.nouns._version import _VERSION

#calss header
class _VERSIONS(_VERSION, ):
	def __init__(self,): 
		_VERSION.__init__(self)
		self.name = "VERSIONS"
		self.specie = 'nouns'
		self.basic = "version"
		self.jsondata = {}
