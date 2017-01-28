

#calss header
class _VEGETARIAN():
	def __init__(self,): 
		self.name = "VEGETARIAN"
		self.definitions = [u'not eating or including meat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
