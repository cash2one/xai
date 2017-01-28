

#calss header
class _PAINFULLY():
	def __init__(self,): 
		self.name = "PAINFULLY"
		self.definitions = [u'in a way that causes pain: ', u'used to emphasize a quality, action, or situation that is unpleasant or not wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
