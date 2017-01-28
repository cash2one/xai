

#calss header
class _NORDIC():
	def __init__(self,): 
		self.name = "NORDIC"
		self.definitions = [u'belonging to or relating to Scandinavia, Finland, or Iceland: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
