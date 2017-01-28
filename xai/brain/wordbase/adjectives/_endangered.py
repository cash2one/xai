

#calss header
class _ENDANGERED():
	def __init__(self,): 
		self.name = "ENDANGERED"
		self.definitions = [u'animals or plants that may soon not exist because there are very few now alive']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
