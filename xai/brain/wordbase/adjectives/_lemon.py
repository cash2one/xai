

#calss header
class _LEMON():
	def __init__(self,): 
		self.name = "LEMON"
		self.definitions = [u'of a pale yellow colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
