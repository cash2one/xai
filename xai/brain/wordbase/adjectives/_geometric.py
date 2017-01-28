

#calss header
class _GEOMETRIC():
	def __init__(self,): 
		self.name = "GEOMETRIC"
		self.definitions = [u'A geometric pattern or arrangement is made up of shapes such as squares, triangles, or rectangles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
