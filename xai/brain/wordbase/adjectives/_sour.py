

#calss header
class _SOUR():
	def __init__(self,): 
		self.name = "SOUR"
		self.definitions = [u'having a sharp, sometimes unpleasant, taste or smell, like a lemon, and not sweet: ', u'unfriendly or easily annoyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
