

#calss header
class _STAPLE():
	def __init__(self,): 
		self.name = "STAPLE"
		self.definitions = [u'basic or main; standard or regular: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
