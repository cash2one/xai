

#calss header
class _BRONZE():
	def __init__(self,): 
		self.name = "BRONZE"
		self.definitions = [u'being dark orange-brown in colour, like the metal bronze']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
