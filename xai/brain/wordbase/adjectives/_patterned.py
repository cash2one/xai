

#calss header
class _PATTERNED():
	def __init__(self,): 
		self.name = "PATTERNED"
		self.definitions = [u'with a design made from repeated lines, shapes, or colours on the surface: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
