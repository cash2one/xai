

#calss header
class _MUSHY():
	def __init__(self,): 
		self.name = "MUSHY"
		self.definitions = [u'soft and having no firm shape: ', u'too emotional: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
