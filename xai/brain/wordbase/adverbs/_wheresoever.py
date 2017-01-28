

#calss header
class _WHERESOEVER():
	def __init__(self,): 
		self.name = "WHERESOEVER"
		self.definitions = [u'formal for  wherever adverb conjunction ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
