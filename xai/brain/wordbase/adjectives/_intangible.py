

#calss header
class _INTANGIBLE():
	def __init__(self,): 
		self.name = "INTANGIBLE"
		self.definitions = [u'An intangible feeling or quality exists but you cannot describe it exactly or prove it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
