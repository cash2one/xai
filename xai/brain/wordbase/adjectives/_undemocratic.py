

#calss header
class _UNDEMOCRATIC():
	def __init__(self,): 
		self.name = "UNDEMOCRATIC"
		self.definitions = [u'not based on the principles of democracy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
