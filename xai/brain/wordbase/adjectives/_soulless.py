

#calss header
class _SOULLESS():
	def __init__(self,): 
		self.name = "SOULLESS"
		self.definitions = [u'showing no human influence or qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
