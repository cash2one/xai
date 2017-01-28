

#calss header
class _FLAGRANT():
	def __init__(self,): 
		self.name = "FLAGRANT"
		self.definitions = [u'(of a bad action, situation, person, etc.) shocking because of being so obvious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
