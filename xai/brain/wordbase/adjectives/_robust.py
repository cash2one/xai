

#calss header
class _ROBUST():
	def __init__(self,): 
		self.name = "ROBUST"
		self.definitions = [u'(of a person or animal) strong and healthy, or (of an object or system) strong and unlikely to break or fail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
