

#calss header
class _LAMINATED():
	def __init__(self,): 
		self.name = "LAMINATED"
		self.definitions = [u'covered with a thin layer of plastic to protect it: ', u'consisting of several thin layers of wood, plastic, glass, etc. stuck together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
