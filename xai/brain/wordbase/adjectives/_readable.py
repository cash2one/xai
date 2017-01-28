

#calss header
class _READABLE():
	def __init__(self,): 
		self.name = "READABLE"
		self.definitions = [u'easy and enjoyable to read: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
