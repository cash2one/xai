

#calss header
class _CATALAN():
	def __init__(self,): 
		self.name = "CATALAN"
		self.definitions = [u'belonging to or relating to Catalonia or its people, or to the Catalan language: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
