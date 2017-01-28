

#calss header
class _SUBHUMAN():
	def __init__(self,): 
		self.name = "SUBHUMAN"
		self.definitions = [u'having or showing behaviour or characteristics that are much worse than those expected of ordinary people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
