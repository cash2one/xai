

#calss header
class _CAPTIOUS():
	def __init__(self,): 
		self.name = "CAPTIOUS"
		self.definitions = [u'often expressing criticisms about matters that are not important']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
