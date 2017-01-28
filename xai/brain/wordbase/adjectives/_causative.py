

#calss header
class _CAUSATIVE():
	def __init__(self,): 
		self.name = "CAUSATIVE"
		self.definitions = [u'acting as the cause of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
