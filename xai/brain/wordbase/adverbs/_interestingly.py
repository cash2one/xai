

#calss header
class _INTERESTINGLY():
	def __init__(self,): 
		self.name = "INTERESTINGLY"
		self.definitions = [u'used to introduce a piece of information that the speaker thinks is strange or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
