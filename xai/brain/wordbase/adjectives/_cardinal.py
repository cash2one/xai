

#calss header
class _CARDINAL():
	def __init__(self,): 
		self.name = "CARDINAL"
		self.definitions = [u'of great importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
