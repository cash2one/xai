

#calss header
class _PICAYUNE():
	def __init__(self,): 
		self.name = "PICAYUNE"
		self.definitions = [u'having little value or importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
