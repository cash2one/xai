

#calss header
class _BRUTE():
	def __init__(self,): 
		self.name = "BRUTE"
		self.definitions = [u'great physical force or strength: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
