

#calss header
class _RADIOACTIVE():
	def __init__(self,): 
		self.name = "RADIOACTIVE"
		self.definitions = [u'having or producing the energy that comes from the breaking up of atoms: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
