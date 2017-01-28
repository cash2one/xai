

#calss header
class _TENFOLD():
	def __init__(self,): 
		self.name = "TENFOLD"
		self.definitions = [u'ten times as big or as much: ', u'having ten parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
