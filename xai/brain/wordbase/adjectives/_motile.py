

#calss header
class _MOTILE():
	def __init__(self,): 
		self.name = "MOTILE"
		self.definitions = [u'(especially of plants, organisms, and very small forms of life) able to move by itself']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
