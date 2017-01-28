

#calss header
class _SOLELY():
	def __init__(self,): 
		self.name = "SOLELY"
		self.definitions = [u'only and not involving anyone or anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
