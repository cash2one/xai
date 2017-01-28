

#calss header
class _DISSOLUTE():
	def __init__(self,): 
		self.name = "DISSOLUTE"
		self.definitions = [u'(of a person) living in a way that other people strongly disapprove of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
