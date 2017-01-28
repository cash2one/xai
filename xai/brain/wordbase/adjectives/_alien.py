

#calss header
class _ALIEN():
	def __init__(self,): 
		self.name = "ALIEN"
		self.definitions = [u'coming from a different country, race, or group: ', u'strange and not familiar: ', u'relating to creatures from another planet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
