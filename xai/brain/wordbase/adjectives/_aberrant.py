

#calss header
class _ABERRANT():
	def __init__(self,): 
		self.name = "ABERRANT"
		self.definitions = [u'different from what is typical or usual, especially in an unacceptable way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
