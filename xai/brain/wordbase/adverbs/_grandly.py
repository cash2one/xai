

#calss header
class _GRANDLY():
	def __init__(self,): 
		self.name = "GRANDLY"
		self.definitions = [u'in a way suggesting that something or someone has great importance: ', u'in a way that attracts admiration and attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
