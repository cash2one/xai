

#calss header
class _GROOVY():
	def __init__(self,): 
		self.name = "GROOVY"
		self.definitions = [u'very fashionable and interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
