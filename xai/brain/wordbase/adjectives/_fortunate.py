

#calss header
class _FORTUNATE():
	def __init__(self,): 
		self.name = "FORTUNATE"
		self.definitions = [u'lucky: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
