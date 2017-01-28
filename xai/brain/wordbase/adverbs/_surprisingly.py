

#calss header
class _SURPRISINGLY():
	def __init__(self,): 
		self.name = "SURPRISINGLY"
		self.definitions = [u'unexpectedly or in a way that is unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
