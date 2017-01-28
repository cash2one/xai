

#calss header
class _BEVELLED():
	def __init__(self,): 
		self.name = "BEVELLED"
		self.definitions = [u'having a sloping edge or surface: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
