

#calss header
class _LANGUID():
	def __init__(self,): 
		self.name = "LANGUID"
		self.definitions = [u'moving or speaking slowly with little energy, often in an attractive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
