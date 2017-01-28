

#calss header
class _BLUNTLY():
	def __init__(self,): 
		self.name = "BLUNTLY"
		self.definitions = [u"If you speak bluntly, you speak without trying to be polite or considering other people's feelings: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
