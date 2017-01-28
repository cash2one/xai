

#calss header
class _GHASTLY():
	def __init__(self,): 
		self.name = "GHASTLY"
		self.definitions = [u'unpleasant and shocking: ', u'extremely bad: ', u'If someone looks ghastly, they look very ill or very shocked, especially with a very pale face: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
