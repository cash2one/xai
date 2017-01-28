

#calss header
class _SKIMPY():
	def __init__(self,): 
		self.name = "SKIMPY"
		self.definitions = [u'not large enough: ', u'Skimpy clothing shows a lot of your body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
