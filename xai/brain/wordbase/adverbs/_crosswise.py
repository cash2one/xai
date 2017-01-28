

#calss header
class _CROSSWISE():
	def __init__(self,): 
		self.name = "CROSSWISE"
		self.definitions = [u'crossing something, especially at an angle of 90\xb0']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
