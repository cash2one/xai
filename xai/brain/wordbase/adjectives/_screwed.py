

#calss header
class _SCREWED():
	def __init__(self,): 
		self.name = "SCREWED"
		self.definitions = [u'in very bad trouble or difficulty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
