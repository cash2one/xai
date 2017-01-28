

#calss header
class _IDYLLIC():
	def __init__(self,): 
		self.name = "IDYLLIC"
		self.definitions = [u'An idyllic place or experience is extremely pleasant, beautiful, or peaceful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
