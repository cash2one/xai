

#calss header
class _TELLTALE():
	def __init__(self,): 
		self.name = "TELLTALE"
		self.definitions = [u'allowing a secret to become known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
