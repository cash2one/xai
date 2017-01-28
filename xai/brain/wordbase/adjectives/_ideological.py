

#calss header
class _IDEOLOGICAL():
	def __init__(self,): 
		self.name = "IDEOLOGICAL"
		self.definitions = [u'based on or relating to a particular set of ideas or beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
