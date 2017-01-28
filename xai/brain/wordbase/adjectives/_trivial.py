

#calss header
class _TRIVIAL():
	def __init__(self,): 
		self.name = "TRIVIAL"
		self.definitions = [u'having little value or importance: ', u'A trivial problem is easy to solve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
