

#calss header
class _PARTICULARLY():
	def __init__(self,): 
		self.name = "PARTICULARLY"
		self.definitions = [u'especially, or more than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
