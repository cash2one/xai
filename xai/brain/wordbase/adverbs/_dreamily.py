

#calss header
class _DREAMILY():
	def __init__(self,): 
		self.name = "DREAMILY"
		self.definitions = [u'If you say or do something dreamily, you do it as if you are not completely awake and are thinking of pleasant things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
