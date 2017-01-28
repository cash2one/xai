

#calss header
class _MERELY():
	def __init__(self,): 
		self.name = "MERELY"
		self.definitions = [u'used to emphasize that you mean exactly what you are saying and nothing more: ', u'used to emphasize that something is not large, important, or effective when compared to something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
