

#calss header
class _CARTESIAN():
	def __init__(self,): 
		self.name = "CARTESIAN"
		self.definitions = [u'of or connected with the ideas and theories of the mathematician Ren\xe9 Descartes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
