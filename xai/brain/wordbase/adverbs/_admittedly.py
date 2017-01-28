

#calss header
class _ADMITTEDLY():
	def __init__(self,): 
		self.name = "ADMITTEDLY"
		self.definitions = [u'used when you are agreeing that something is true, especially unwillingly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
