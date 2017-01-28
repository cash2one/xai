

#calss header
class _RECYCLED():
	def __init__(self,): 
		self.name = "RECYCLED"
		self.definitions = [u'having been used before and then put through a process so that it can form a new product: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
