

#calss header
class _TIDAL():
	def __init__(self,): 
		self.name = "TIDAL"
		self.definitions = [u'relating to the tide: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
