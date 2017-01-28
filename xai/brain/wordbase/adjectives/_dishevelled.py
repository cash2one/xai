

#calss header
class _DISHEVELLED():
	def __init__(self,): 
		self.name = "DISHEVELLED"
		self.definitions = [u'(of people or their appearance) very untidy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
