

#calss header
class _HENCE():
	def __init__(self,): 
		self.name = "HENCE"
		self.definitions = [u'that is the reason or explanation for: ', u'from this time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
