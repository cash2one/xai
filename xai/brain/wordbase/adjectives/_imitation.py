

#calss header
class _IMITATION():
	def __init__(self,): 
		self.name = "IMITATION"
		self.definitions = [u'made to look like something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
