

#calss header
class _IMPROVIDENT():
	def __init__(self,): 
		self.name = "IMPROVIDENT"
		self.definitions = [u'not planning carefully for the future, especially by spending money in a way that is unwise']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
