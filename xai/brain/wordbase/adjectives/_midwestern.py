

#calss header
class _MIDWESTERN():
	def __init__(self,): 
		self.name = "MIDWESTERN"
		self.definitions = [u'relating to the Midwest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
