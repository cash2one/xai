

#calss header
class _PROFICIENT():
	def __init__(self,): 
		self.name = "PROFICIENT"
		self.definitions = [u'skilled and experienced: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
