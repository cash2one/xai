

#calss header
class _FLOURISHING():
	def __init__(self,): 
		self.name = "FLOURISHING"
		self.definitions = [u'growing or developing successfully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
