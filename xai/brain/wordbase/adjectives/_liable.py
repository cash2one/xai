

#calss header
class _LIABLE():
	def __init__(self,): 
		self.name = "LIABLE"
		self.definitions = [u'having (legal) responsibility for something or someone: ', u'very likely to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
