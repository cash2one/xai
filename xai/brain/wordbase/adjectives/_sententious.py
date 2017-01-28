

#calss header
class _SENTENTIOUS():
	def __init__(self,): 
		self.name = "SENTENTIOUS"
		self.definitions = [u'trying to appear wise, intelligent, and important, in a way that is annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
