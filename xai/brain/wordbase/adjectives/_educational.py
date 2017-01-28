

#calss header
class _EDUCATIONAL():
	def __init__(self,): 
		self.name = "EDUCATIONAL"
		self.definitions = [u'providing education or relating to education: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
