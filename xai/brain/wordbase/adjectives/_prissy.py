

#calss header
class _PRISSY():
	def __init__(self,): 
		self.name = "PRISSY"
		self.definitions = [u'caring too much about behaving and dressing in a way that is considered correct and that does not shock: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
