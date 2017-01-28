

#calss header
class _CRASS():
	def __init__(self,): 
		self.name = "CRASS"
		self.definitions = [u'stupid and without considering how other people might feel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
