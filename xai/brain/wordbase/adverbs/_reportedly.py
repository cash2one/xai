

#calss header
class _REPORTEDLY():
	def __init__(self,): 
		self.name = "REPORTEDLY"
		self.definitions = [u'according to what many people say: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
