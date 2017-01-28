

#calss header
class _PLASTIC():
	def __init__(self,): 
		self.name = "PLASTIC"
		self.definitions = [u'made of plastic: ', u'artificial or false: ', u'soft enough to be changed into a new shape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
