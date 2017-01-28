

#calss header
class _DRIED():
	def __init__(self,): 
		self.name = "DRIED"
		self.definitions = [u'Dried food or plants have had all their liquid removed, especially in order to stop them from decaying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
