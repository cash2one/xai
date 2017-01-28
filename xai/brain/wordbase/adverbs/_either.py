

#calss header
class _EITHER():
	def __init__(self,): 
		self.name = "EITHER"
		self.definitions = [u'used in negative sentences instead of "also" or "too": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
