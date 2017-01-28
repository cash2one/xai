

#calss header
class _OFFENDING():
	def __init__(self,): 
		self.name = "OFFENDING"
		self.definitions = [u'unwanted, often because unpleasant and causing problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
