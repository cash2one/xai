

#calss header
class _FREELANCE():
	def __init__(self,): 
		self.name = "FREELANCE"
		self.definitions = [u'doing particular pieces of work for different organizations, rather than working all the time for a single organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
