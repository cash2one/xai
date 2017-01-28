

#calss header
class _INC():
	def __init__(self,): 
		self.name = "INC"
		self.definitions = [u'abbreviation for incorporated: used in the names of US companies that are legally established: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
