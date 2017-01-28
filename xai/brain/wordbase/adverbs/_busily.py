

#calss header
class _BUSILY():
	def __init__(self,): 
		self.name = "BUSILY"
		self.definitions = [u'in a busy, active way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
