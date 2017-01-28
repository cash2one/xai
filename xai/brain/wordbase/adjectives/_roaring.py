

#calss header
class _ROARING():
	def __init__(self,): 
		self.name = "ROARING"
		self.definitions = [u'loud and powerful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
