

#calss header
class _SOUNDLY():
	def __init__(self,): 
		self.name = "SOUNDLY"
		self.definitions = [u'completely: ', u'(of how someone sleeps) deeply: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
