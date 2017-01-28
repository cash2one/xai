

#calss header
class _BASS():
	def __init__(self,): 
		self.name = "BASS"
		self.definitions = [u'playing, singing, or producing the lowest range of musical notes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
