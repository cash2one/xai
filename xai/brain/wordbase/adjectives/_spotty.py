

#calss header
class _SPOTTY():
	def __init__(self,): 
		self.name = "SPOTTY"
		self.definitions = [u'used to describe a person with spots on their skin: ', u'bad in some parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
