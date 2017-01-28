

#calss header
class _IMPASSABLE():
	def __init__(self,): 
		self.name = "IMPASSABLE"
		self.definitions = [u'An impassable road or path cannot be travelled on because of bad weather conditions or because it is blocked: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
