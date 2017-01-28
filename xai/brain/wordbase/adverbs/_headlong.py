

#calss header
class _HEADLONG():
	def __init__(self,): 
		self.name = "HEADLONG"
		self.definitions = [u'with great speed or without thinking: ', u'\u2192\xa0 head-first ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
