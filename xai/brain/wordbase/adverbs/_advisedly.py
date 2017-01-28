

#calss header
class _ADVISEDLY():
	def __init__(self,): 
		self.name = "ADVISEDLY"
		self.definitions = [u'If you say you are using a word advisedly, you mean you are choosing it after thinking about it very carefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
