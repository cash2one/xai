

#calss header
class _STREAKY():
	def __init__(self,): 
		self.name = "STREAKY"
		self.definitions = [u'covered with long, thin lines: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
