

#calss header
class _SUPPORTING():
	def __init__(self,): 
		self.name = "SUPPORTING"
		self.definitions = [u'not the most important actor or part in a film or play: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
