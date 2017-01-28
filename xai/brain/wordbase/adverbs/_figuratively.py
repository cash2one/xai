

#calss header
class _FIGURATIVELY():
	def __init__(self,): 
		self.name = "FIGURATIVELY"
		self.definitions = [u'in a way that uses words and phrases with a more imaginative meaning than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
