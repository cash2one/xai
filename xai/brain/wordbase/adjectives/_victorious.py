

#calss header
class _VICTORIOUS():
	def __init__(self,): 
		self.name = "VICTORIOUS"
		self.definitions = [u'having won a game, competition, election, war, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
