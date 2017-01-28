

#calss header
class _EVENTUALLY():
	def __init__(self,): 
		self.name = "EVENTUALLY"
		self.definitions = [u'in the end, especially after a long time or a lot of effort, problems, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
