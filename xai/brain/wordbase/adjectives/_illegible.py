

#calss header
class _ILLEGIBLE():
	def __init__(self,): 
		self.name = "ILLEGIBLE"
		self.definitions = [u'(of writing or print) impossible or almost impossible to read because of being very untidy or not clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
