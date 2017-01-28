

#calss header
class _DICEY():
	def __init__(self,): 
		self.name = "DICEY"
		self.definitions = [u'slightly dangerous or uncertain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
