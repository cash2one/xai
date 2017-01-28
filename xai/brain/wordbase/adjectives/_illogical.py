

#calss header
class _ILLOGICAL():
	def __init__(self,): 
		self.name = "ILLOGICAL"
		self.definitions = [u'not reasonable, wise, or practical, usually because directed by the emotions rather than by careful thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
