

#calss header
class _BRANDED():
	def __init__(self,): 
		self.name = "BRANDED"
		self.definitions = [u'made by a particular company and sold under a particular name: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
