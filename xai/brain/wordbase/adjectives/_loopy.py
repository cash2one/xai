

#calss header
class _LOOPY():
	def __init__(self,): 
		self.name = "LOOPY"
		self.definitions = [u'strange, unusual, or silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
