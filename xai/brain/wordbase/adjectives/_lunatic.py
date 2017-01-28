

#calss header
class _LUNATIC():
	def __init__(self,): 
		self.name = "LUNATIC"
		self.definitions = [u'silly in a dangerous way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
