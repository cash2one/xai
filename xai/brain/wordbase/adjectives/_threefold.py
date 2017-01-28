

#calss header
class _THREEFOLD():
	def __init__(self,): 
		self.name = "THREEFOLD"
		self.definitions = [u'three times as big or as much: ', u'having three parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
