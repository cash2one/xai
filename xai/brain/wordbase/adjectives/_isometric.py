

#calss header
class _ISOMETRIC():
	def __init__(self,): 
		self.name = "ISOMETRIC"
		self.definitions = [u'Isometric drawing uses a method of drawing a shape with three dimensions using two dimensions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
