

#calss header
class _TWOFOLD():
	def __init__(self,): 
		self.name = "TWOFOLD"
		self.definitions = [u'twice as big or as much: ', u'having two parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
