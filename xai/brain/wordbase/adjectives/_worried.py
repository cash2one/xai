

#calss header
class _WORRIED():
	def __init__(self,): 
		self.name = "WORRIED"
		self.definitions = [u'unhappy because you are thinking about problems or unpleasant things that might happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
