

#calss header
class _FLAMMABLE():
	def __init__(self,): 
		self.name = "FLAMMABLE"
		self.definitions = [u'Something that is flammable burns easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
