

#calss header
class _COSMOPOLITAN():
	def __init__(self,): 
		self.name = "COSMOPOLITAN"
		self.definitions = [u'containing or having experience of people and things from many different parts of the world: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
