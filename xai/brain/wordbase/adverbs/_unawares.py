

#calss header
class _UNAWARES():
	def __init__(self,): 
		self.name = "UNAWARES"
		self.definitions = [u'suddenly and unexpectedly without any warning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
