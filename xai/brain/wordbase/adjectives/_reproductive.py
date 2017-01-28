

#calss header
class _REPRODUCTIVE():
	def __init__(self,): 
		self.name = "REPRODUCTIVE"
		self.definitions = [u'relating to the process of reproduction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
