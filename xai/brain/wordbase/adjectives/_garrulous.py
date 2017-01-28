

#calss header
class _GARRULOUS():
	def __init__(self,): 
		self.name = "GARRULOUS"
		self.definitions = [u'having the habit of talking a lot, especially about things that are not important']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
