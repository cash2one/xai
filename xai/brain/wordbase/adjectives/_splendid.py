

#calss header
class _SPLENDID():
	def __init__(self,): 
		self.name = "SPLENDID"
		self.definitions = [u'excellent, or beautiful and impressive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
