

#calss header
class _HITHERTO():
	def __init__(self,): 
		self.name = "HITHERTO"
		self.definitions = [u'until now or until a particular time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
