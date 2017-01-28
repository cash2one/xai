

#calss header
class _UNPARALLELED():
	def __init__(self,): 
		self.name = "UNPARALLELED"
		self.definitions = [u'having no equal; better or greater than any other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
