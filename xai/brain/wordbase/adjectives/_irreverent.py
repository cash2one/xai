

#calss header
class _IRREVERENT():
	def __init__(self,): 
		self.name = "IRREVERENT"
		self.definitions = [u'not showing the expected respect for official, important, or holy things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
