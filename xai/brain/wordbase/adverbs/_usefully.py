

#calss header
class _USEFULLY():
	def __init__(self,): 
		self.name = "USEFULLY"
		self.definitions = [u'in an effective or helpful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
