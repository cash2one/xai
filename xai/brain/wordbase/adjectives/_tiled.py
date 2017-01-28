

#calss header
class _TILED():
	def __init__(self,): 
		self.name = "TILED"
		self.definitions = [u'(of a surface) covered with tiles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
