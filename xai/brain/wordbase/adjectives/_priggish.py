

#calss header
class _PRIGGISH():
	def __init__(self,): 
		self.name = "PRIGGISH"
		self.definitions = [u'like a prig: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
