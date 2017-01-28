

#calss header
class _JUST():
	def __init__(self,): 
		self.name = "JUST"
		self.definitions = [u'now, very soon, or very recently: ', u'a very short time ago: ', u'at the present time: ', u'exactly or equally: ', u'only; simply: ', u'used to make a statement or order stronger: ', u'used to reduce the force of a statement and to suggest that it is not very important: ', u'almost not or almost: ', u'If something is just possible, there is a slight chance that it will happen: ', u'very; completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
