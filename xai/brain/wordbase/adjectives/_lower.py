

#calss header
class _LOWER():
	def __init__(self,): 
		self.name = "LOWER"
		self.definitions = [u'positioned below one or more similar things, or of the bottom part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
