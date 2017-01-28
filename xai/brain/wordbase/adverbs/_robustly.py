

#calss header
class _ROBUSTLY():
	def __init__(self,): 
		self.name = "ROBUSTLY"
		self.definitions = [u'If you do something robustly, you do it in a determined way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
