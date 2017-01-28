

#calss header
class _OVERQUALIFIED():
	def __init__(self,): 
		self.name = "OVERQUALIFIED"
		self.definitions = [u'having more knowledge, skill, and/or experience than is needed (for a particular job): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
