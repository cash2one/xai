

#calss header
class _CUMULATIVE():
	def __init__(self,): 
		self.name = "CUMULATIVE"
		self.definitions = [u'increasing by one addition after another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
