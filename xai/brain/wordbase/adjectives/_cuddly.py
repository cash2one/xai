

#calss header
class _CUDDLY():
	def __init__(self,): 
		self.name = "CUDDLY"
		self.definitions = [u'liking to cuddle, or making you want to cuddle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
