

#calss header
class _WOODED():
	def __init__(self,): 
		self.name = "WOODED"
		self.definitions = [u'covered with trees: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
