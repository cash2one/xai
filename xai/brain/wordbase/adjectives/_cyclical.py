

#calss header
class _CYCLICAL():
	def __init__(self,): 
		self.name = "CYCLICAL"
		self.definitions = [u'Cyclical events happen in a particular order, one following the other, and are often repeated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
