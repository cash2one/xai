

#calss header
class _THINLY():
	def __init__(self,): 
		self.name = "THINLY"
		self.definitions = [u'made or done so that something is not thick: ', u'with only a small number of people or things, or without the people or things being close to each other: ', u'in a way that is not difficult to see through or to recognize: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
