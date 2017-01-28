

#calss header
class _WIRY():
	def __init__(self,): 
		self.name = "WIRY"
		self.definitions = [u'(of people and animals) thin but strong, and often able to bend easily: ', u'Wiry hair is strong, thick, and rough to touch.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
