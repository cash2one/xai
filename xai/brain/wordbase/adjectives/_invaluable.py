

#calss header
class _INVALUABLE():
	def __init__(self,): 
		self.name = "INVALUABLE"
		self.definitions = [u'extremely useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
