

#calss header
class _GOLDEN():
	def __init__(self,): 
		self.name = "GOLDEN"
		self.definitions = [u'made of gold: ', u'the colour of gold: ', u'special, successful, or giving someone an advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
