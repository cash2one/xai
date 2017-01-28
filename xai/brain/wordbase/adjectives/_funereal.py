

#calss header
class _FUNEREAL():
	def __init__(self,): 
		self.name = "FUNEREAL"
		self.definitions = [u'suitable for a funeral: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
