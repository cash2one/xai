

#calss header
class _MARKED():
	def __init__(self,): 
		self.name = "MARKED"
		self.definitions = [u'A marked change or difference in behaviour or in a situation is very obvious or noticeable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
