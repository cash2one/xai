

#calss header
class _UNRELATED():
	def __init__(self,): 
		self.name = "UNRELATED"
		self.definitions = [u'having no connection: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
