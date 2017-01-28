

#calss header
class _LILTING():
	def __init__(self,): 
		self.name = "LILTING"
		self.definitions = [u'A lilting voice or tune gently rises and falls in a way that is pleasant to listen to.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
