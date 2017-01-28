

#calss header
class _ONLINE():
	def __init__(self,): 
		self.name = "ONLINE"
		self.definitions = [u'bought, used, etc. using the internet: ', u'to be able to use email or the internet: ', u'connected to a system: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
