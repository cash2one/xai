

#calss header
class _WISPY():
	def __init__(self,): 
		self.name = "WISPY"
		self.definitions = [u'in the form of a wisp or wisps: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
