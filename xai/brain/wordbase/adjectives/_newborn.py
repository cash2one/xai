

#calss header
class _NEWBORN():
	def __init__(self,): 
		self.name = "NEWBORN"
		self.definitions = [u'recently born: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
