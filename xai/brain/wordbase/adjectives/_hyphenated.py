

#calss header
class _HYPHENATED():
	def __init__(self,): 
		self.name = "HYPHENATED"
		self.definitions = [u'written with a hyphen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
