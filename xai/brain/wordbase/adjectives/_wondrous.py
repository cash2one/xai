

#calss header
class _WONDROUS():
	def __init__(self,): 
		self.name = "WONDROUS"
		self.definitions = [u'extremely and surprisingly good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
