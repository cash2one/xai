

#calss header
class _ICKY():
	def __init__(self,): 
		self.name = "ICKY"
		self.definitions = [u'unpleasant, especially to look at: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
