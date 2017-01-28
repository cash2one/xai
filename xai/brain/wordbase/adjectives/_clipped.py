

#calss header
class _CLIPPED():
	def __init__(self,): 
		self.name = "CLIPPED"
		self.definitions = [u'with words pronounced quickly and clearly, sometimes with parts missing, or in a very short and unfriendly way: ', u'cut short and tidy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
