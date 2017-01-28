

#calss header
class _SHAGGY():
	def __init__(self,): 
		self.name = "SHAGGY"
		self.definitions = [u'having or covered with long, rough, and untidy hair, or (of hair) long, rough, and untidy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
