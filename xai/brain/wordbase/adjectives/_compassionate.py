

#calss header
class _COMPASSIONATE():
	def __init__(self,): 
		self.name = "COMPASSIONATE"
		self.definitions = [u'showing compassion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
