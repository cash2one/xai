

#calss header
class _NERVOUSLY():
	def __init__(self,): 
		self.name = "NERVOUSLY"
		self.definitions = [u'feeling or showing that you are worried and anxious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
