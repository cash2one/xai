

#calss header
class _GUILTLESS():
	def __init__(self,): 
		self.name = "GUILTLESS"
		self.definitions = [u'not responsible for doing something wrong or committing a crime']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
