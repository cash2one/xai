

#calss header
class _CORPORAL():
	def __init__(self,): 
		self.name = "CORPORAL"
		self.definitions = [u'of or relating to the body']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
