

#calss header
class _PROMPT():
	def __init__(self,): 
		self.name = "PROMPT"
		self.definitions = [u'at the time stated and no later: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
