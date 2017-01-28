

#calss header
class _SCRAPPY():
	def __init__(self,): 
		self.name = "SCRAPPY"
		self.definitions = [u'badly organized or put together: ', u'untidy and not very attractive or well developed: ', u'having a strong, determined character, and willing to argue or fight for what you want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
