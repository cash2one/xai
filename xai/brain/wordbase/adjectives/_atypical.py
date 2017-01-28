

#calss header
class _ATYPICAL():
	def __init__(self,): 
		self.name = "ATYPICAL"
		self.definitions = [u'different from all others of the same type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
