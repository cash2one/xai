

#calss header
class _DITTO():
	def __init__(self,): 
		self.name = "DITTO"
		self.definitions = [u'used to agree with something that has just been said, or to avoid repeating something that has been said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
