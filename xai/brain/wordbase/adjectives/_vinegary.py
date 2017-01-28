

#calss header
class _VINEGARY():
	def __init__(self,): 
		self.name = "VINEGARY"
		self.definitions = [u'tasting or smelling like vinegar: ', u'angry and unpleasant, or giving a lot of criticism: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
