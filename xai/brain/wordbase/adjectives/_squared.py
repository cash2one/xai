

#calss header
class _SQUARED():
	def __init__(self,): 
		self.name = "SQUARED"
		self.definitions = [u'covered with squares: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
