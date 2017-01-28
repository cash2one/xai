

#calss header
class _UNTHINKING():
	def __init__(self,): 
		self.name = "UNTHINKING"
		self.definitions = [u'not based on serious thought or an examination of the information: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
