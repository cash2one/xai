

#calss header
class _ZIPPY():
	def __init__(self,): 
		self.name = "ZIPPY"
		self.definitions = [u'energetic or fast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
