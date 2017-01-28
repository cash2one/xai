

#calss header
class _PARAMILITARY():
	def __init__(self,): 
		self.name = "PARAMILITARY"
		self.definitions = [u'A paramilitary group is organized like an army but is not official and often not legal.', u'connected with and helping the official armed forces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
