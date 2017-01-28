

#calss header
class _POINTY():
	def __init__(self,): 
		self.name = "POINTY"
		self.definitions = [u'shaped into a point: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
