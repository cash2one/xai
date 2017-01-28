

#calss header
class _GROOMED():
	def __init__(self,): 
		self.name = "GROOMED"
		self.definitions = [u'having a clean and neat appearance that is produced with care: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
