

#calss header
class _GEOCENTRIC():
	def __init__(self,): 
		self.name = "GEOCENTRIC"
		self.definitions = [u'having the earth as its centre']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
