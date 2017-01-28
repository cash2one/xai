

#calss header
class _OVERHEATED():
	def __init__(self,): 
		self.name = "OVERHEATED"
		self.definitions = [u'If a situation is/gets overheated, strong feelings, especially anger, are expressed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
