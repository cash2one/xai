

#calss header
class _SATINY():
	def __init__(self,): 
		self.name = "SATINY"
		self.definitions = [u'smooth and soft']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
