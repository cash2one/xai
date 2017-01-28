

#calss header
class _TIBETAN():
	def __init__(self,): 
		self.name = "TIBETAN"
		self.definitions = [u'belonging or relating to Tibet, its people, or its language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
