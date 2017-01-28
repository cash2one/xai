

#calss header
class _CRIMINAL():
	def __init__(self,): 
		self.name = "CRIMINAL"
		self.definitions = [u'relating to crime: ', u'very bad or morally wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
