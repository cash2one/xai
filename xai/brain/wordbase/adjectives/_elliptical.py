

#calss header
class _ELLIPTICAL():
	def __init__(self,): 
		self.name = "ELLIPTICAL"
		self.definitions = [u'having an oval shape', u'Elliptical language has parts missing, so that it is sometimes difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
