

#calss header
class _HOPEFULLY():
	def __init__(self,): 
		self.name = "HOPEFULLY"
		self.definitions = [u'used, often at the start of a sentence, to express what you would like to happen: ', u'in a hopeful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
