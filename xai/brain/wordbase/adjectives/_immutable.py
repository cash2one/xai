

#calss header
class _IMMUTABLE():
	def __init__(self,): 
		self.name = "IMMUTABLE"
		self.definitions = [u'not changing, or unable to be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
