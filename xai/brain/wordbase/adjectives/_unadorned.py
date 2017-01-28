

#calss header
class _UNADORNED():
	def __init__(self,): 
		self.name = "UNADORNED"
		self.definitions = [u'plain and simple, with little or no decoration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
