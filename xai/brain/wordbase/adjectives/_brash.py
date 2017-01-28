

#calss header
class _BRASH():
	def __init__(self,): 
		self.name = "BRASH"
		self.definitions = [u'(of people) showing too much confidence and too little respect: ', u'(of clothes) too bright and colourful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
