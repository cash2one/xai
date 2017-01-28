

#calss header
class _DISREPUTABLE():
	def __init__(self,): 
		self.name = "DISREPUTABLE"
		self.definitions = [u'not trusted or respected; thought to have a bad character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
