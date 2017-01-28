

#calss header
class _ABIDING():
	def __init__(self,): 
		self.name = "ABIDING"
		self.definitions = [u'An abiding feeling or memory is one that you have had for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
