

#calss header
class _CRUMBLY():
	def __init__(self,): 
		self.name = "CRUMBLY"
		self.definitions = [u'breaking easily into small pieces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
