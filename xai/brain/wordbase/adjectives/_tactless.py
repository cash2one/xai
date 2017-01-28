

#calss header
class _TACTLESS():
	def __init__(self,): 
		self.name = "TACTLESS"
		self.definitions = [u'not careful about saying or doing something that could upset someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
