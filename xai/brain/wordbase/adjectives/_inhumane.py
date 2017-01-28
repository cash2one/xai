

#calss header
class _INHUMANE():
	def __init__(self,): 
		self.name = "INHUMANE"
		self.definitions = [u'cruel and causing suffering to people or animals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
