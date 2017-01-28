

#calss header
class _PLEISTOCENE():
	def __init__(self,): 
		self.name = "PLEISTOCENE"
		self.definitions = [u'from or referring to the period of time between around 1.8 million and 11,000 years ago, in which modern humans first appeared, and the Northern Hemisphere experienced an ice age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
