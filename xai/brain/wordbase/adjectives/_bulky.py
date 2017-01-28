

#calss header
class _BULKY():
	def __init__(self,): 
		self.name = "BULKY"
		self.definitions = [u'too big and taking up too much space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
