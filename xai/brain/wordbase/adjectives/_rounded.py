

#calss header
class _ROUNDED():
	def __init__(self,): 
		self.name = "ROUNDED"
		self.definitions = [u'round or curved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
