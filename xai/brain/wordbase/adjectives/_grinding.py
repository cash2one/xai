

#calss header
class _GRINDING():
	def __init__(self,): 
		self.name = "GRINDING"
		self.definitions = [u'a situation in which people are extremely poor over a long period']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
