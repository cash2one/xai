

#calss header
class _COEVAL():
	def __init__(self,): 
		self.name = "COEVAL"
		self.definitions = [u'of the same age or existing at the same time as another person or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
