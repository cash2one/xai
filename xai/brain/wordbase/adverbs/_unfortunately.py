

#calss header
class _UNFORTUNATELY():
	def __init__(self,): 
		self.name = "UNFORTUNATELY"
		self.definitions = [u'used to say that something is sad, disappointing, or has a bad effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
