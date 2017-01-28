

#calss header
class _HEAVING():
	def __init__(self,): 
		self.name = "HEAVING"
		self.definitions = [u'full of people: ', u'moving in large movements up and down: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
