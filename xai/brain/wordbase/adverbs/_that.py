

#calss header
class _THAT():
	def __init__(self,): 
		self.name = "THAT"
		self.definitions = [u'as much as suggested: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
