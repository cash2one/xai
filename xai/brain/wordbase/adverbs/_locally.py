

#calss header
class _LOCALLY():
	def __init__(self,): 
		self.name = "LOCALLY"
		self.definitions = [u'in the particular small area that you are talking about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
