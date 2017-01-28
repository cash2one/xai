

#calss header
class _ESPECIALLY():
	def __init__(self,): 
		self.name = "ESPECIALLY"
		self.definitions = [u'very much; more than usual or more than other people or things: ', u'for a particular reason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
