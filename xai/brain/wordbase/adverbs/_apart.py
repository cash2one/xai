

#calss header
class _APART():
	def __init__(self,): 
		self.name = "APART"
		self.definitions = [u'separated by a distance or by time: ', u'into smaller pieces: ', u'except for or not considering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
