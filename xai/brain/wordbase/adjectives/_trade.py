

#calss header
class _TRADE():
	def __init__(self,): 
		self.name = "TRADE"
		self.definitions = [u'a newspaper, etc. produced for people working in a particular business or industry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
