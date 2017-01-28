

#calss header
class _OVERALL():
	def __init__(self,): 
		self.name = "OVERALL"
		self.definitions = [u'in general rather than in particular, or including all the people or things in a particular group or situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
