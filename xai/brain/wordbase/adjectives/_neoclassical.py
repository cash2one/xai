

#calss header
class _NEOCLASSICAL():
	def __init__(self,): 
		self.name = "NEOCLASSICAL"
		self.definitions = [u'made in a style that is based on the art and building designs of ancient Greece and Rome']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
