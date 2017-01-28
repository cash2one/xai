

#calss header
class _HYPERSENSITIVE():
	def __init__(self,): 
		self.name = "HYPERSENSITIVE"
		self.definitions = [u'too easily upset by criticism: ', u'very easily influenced, changed, or damaged, especially by a physical activity or effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
