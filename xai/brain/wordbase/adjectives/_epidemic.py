

#calss header
class _EPIDEMIC():
	def __init__(self,): 
		self.name = "EPIDEMIC"
		self.definitions = [u'happening a lot and affecting many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
