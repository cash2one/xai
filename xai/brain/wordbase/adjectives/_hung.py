

#calss header
class _HUNG():
	def __init__(self,): 
		self.name = "HUNG"
		self.definitions = [u'having an equal or nearly equal number of members with opposing opinions, so that no decisions can be made: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
