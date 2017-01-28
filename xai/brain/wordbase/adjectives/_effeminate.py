

#calss header
class _EFFEMINATE():
	def __init__(self,): 
		self.name = "EFFEMINATE"
		self.definitions = [u'An effeminate man behaves or looks similar to a woman: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
