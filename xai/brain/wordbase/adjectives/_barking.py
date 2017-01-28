

#calss header
class _BARKING():
	def __init__(self,): 
		self.name = "BARKING"
		self.definitions = [u'crazy or extremely silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
