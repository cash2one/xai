

#calss header
class _HENCEFORTH():
	def __init__(self,): 
		self.name = "HENCEFORTH"
		self.definitions = [u'starting from this time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
