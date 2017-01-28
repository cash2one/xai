

#calss header
class _UBIQUITOUS():
	def __init__(self,): 
		self.name = "UBIQUITOUS"
		self.definitions = [u'seeming to be everywhere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
