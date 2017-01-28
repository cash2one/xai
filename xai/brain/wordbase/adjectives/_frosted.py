

#calss header
class _FROSTED():
	def __init__(self,): 
		self.name = "FROSTED"
		self.definitions = [u'Frosted glass is less smooth to stop it being transparent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
