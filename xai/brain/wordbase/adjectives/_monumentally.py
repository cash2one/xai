

#calss header
class _MONUMENTALLY():
	def __init__(self,): 
		self.name = "MONUMENTALLY"
		self.definitions = [u'extremely (usually used when describing something in a negative way): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
