

#calss header
class _CONTINUOUS():
	def __init__(self,): 
		self.name = "CONTINUOUS"
		self.definitions = [u'without a pause or interruption: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
