

#calss header
class _BAWDY():
	def __init__(self,): 
		self.name = "BAWDY"
		self.definitions = [u'containing humorous remarks about sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
