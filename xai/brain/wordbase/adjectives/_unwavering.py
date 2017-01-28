

#calss header
class _UNWAVERING():
	def __init__(self,): 
		self.name = "UNWAVERING"
		self.definitions = [u'never moving or looking away from something: ', u'never changing or becoming weaker: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
