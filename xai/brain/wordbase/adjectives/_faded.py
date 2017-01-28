

#calss header
class _FADED():
	def __init__(self,): 
		self.name = "FADED"
		self.definitions = [u'less bright in colour than before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
