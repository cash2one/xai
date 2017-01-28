

#calss header
class _PIQUANT():
	def __init__(self,): 
		self.name = "PIQUANT"
		self.definitions = [u'interesting and exciting, especially because of being mysterious: ', u'having a pleasant sharp or spicy taste: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
