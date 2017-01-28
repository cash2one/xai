

#calss header
class _LEGIBLE():
	def __init__(self,): 
		self.name = "LEGIBLE"
		self.definitions = [u'Legible writing or print can be read easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
