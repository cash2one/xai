

#calss header
class _PRESCIENT():
	def __init__(self,): 
		self.name = "PRESCIENT"
		self.definitions = [u'knowing or suggesting correctly what will happen in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
