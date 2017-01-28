

#calss header
class _CRUSHING():
	def __init__(self,): 
		self.name = "CRUSHING"
		self.definitions = [u'severe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
