

#calss header
class _NEONATAL():
	def __init__(self,): 
		self.name = "NEONATAL"
		self.definitions = [u'of or for babies that were born recently: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
