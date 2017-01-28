

#calss header
class _NTH():
	def __init__(self,): 
		self.name = "NTH"
		self.definitions = [u'used to describe the most recent in a long series of things, when you do not know how many there are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
