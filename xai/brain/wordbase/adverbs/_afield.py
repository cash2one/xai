

#calss header
class _AFIELD():
	def __init__(self,): 
		self.name = "AFIELD"
		self.definitions = [u'a long/longer distance away: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
