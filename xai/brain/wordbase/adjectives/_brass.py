

#calss header
class _BRASS():
	def __init__(self,): 
		self.name = "BRASS"
		self.definitions = [u'(of a musical instrument) made of metal and played by blowing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
