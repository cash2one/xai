

#calss header
class _LANK():
	def __init__(self,): 
		self.name = "LANK"
		self.definitions = [u'Lank hair is not attractive because it is completely straight and thin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
