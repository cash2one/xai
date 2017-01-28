

#calss header
class _BRACKISH():
	def __init__(self,): 
		self.name = "BRACKISH"
		self.definitions = [u'Brackish water is salty, dirty, and unpleasant.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
