

#calss header
class _INEFFECTIVE():
	def __init__(self,): 
		self.name = "INEFFECTIVE"
		self.definitions = [u'not producing the effects or results that are wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
