

#calss header
class _SALUBRIOUS():
	def __init__(self,): 
		self.name = "SALUBRIOUS"
		self.definitions = [u'A salubrious place is pleasant, clean, and healthy to live in: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
