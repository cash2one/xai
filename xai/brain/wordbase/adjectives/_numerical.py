

#calss header
class _NUMERICAL():
	def __init__(self,): 
		self.name = "NUMERICAL"
		self.definitions = [u'involving or expressed in numbers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
