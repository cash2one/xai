

#calss header
class _ERSATZ():
	def __init__(self,): 
		self.name = "ERSATZ"
		self.definitions = [u'used instead of something else, usually because the other thing is too expensive or rare: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
