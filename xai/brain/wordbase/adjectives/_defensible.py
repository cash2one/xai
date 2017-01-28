

#calss header
class _DEFENSIBLE():
	def __init__(self,): 
		self.name = "DEFENSIBLE"
		self.definitions = [u'able to be protected from attack, or able to be supported by argument: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
