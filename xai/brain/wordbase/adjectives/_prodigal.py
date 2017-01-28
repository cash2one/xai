

#calss header
class _PRODIGAL():
	def __init__(self,): 
		self.name = "PRODIGAL"
		self.definitions = [u'spending large amounts of money without thinking of the future, in a way that is not wise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
