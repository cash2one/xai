

#calss header
class _SCREWBALL():
	def __init__(self,): 
		self.name = "SCREWBALL"
		self.definitions = [u'used to describe a type of film in which there are funny characters and silly situations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
