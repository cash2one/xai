

#calss header
class _SHADY():
	def __init__(self,): 
		self.name = "SHADY"
		self.definitions = [u'sheltered from direct light from the sun: ', u'dishonest or illegal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
