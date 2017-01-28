

#calss header
class _AGGRESSIVE():
	def __init__(self,): 
		self.name = "AGGRESSIVE"
		self.definitions = [u'behaving in an angry and violent way towards another person: ', u'determined to win or succeed and using forceful action to win or to achieve success: ', u'An aggressive disease is one that spreads quickly and has little chance of being cured: ', u'used to describe a very strong treatment for a serious condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
