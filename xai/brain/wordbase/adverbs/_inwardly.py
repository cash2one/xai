

#calss header
class _INWARDLY():
	def __init__(self,): 
		self.name = "INWARDLY"
		self.definitions = [u'inside your mind and not expressed to other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
