

#calss header
class _CORPOREAL():
	def __init__(self,): 
		self.name = "CORPOREAL"
		self.definitions = [u'physical and not spiritual', u'relating to the body']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
