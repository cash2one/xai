

#calss header
class _INFANTILE():
	def __init__(self,): 
		self.name = "INFANTILE"
		self.definitions = [u'typical of a child and therefore unsuitable for an adult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
