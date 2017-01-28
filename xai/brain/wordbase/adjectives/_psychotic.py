

#calss header
class _PSYCHOTIC():
	def __init__(self,): 
		self.name = "PSYCHOTIC"
		self.definitions = [u'suffering from psychosis (= severe mental disease): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
