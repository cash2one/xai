

#calss header
class _SUPERB():
	def __init__(self,): 
		self.name = "SUPERB"
		self.definitions = [u'of excellent quality; very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
