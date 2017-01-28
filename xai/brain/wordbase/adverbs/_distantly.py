

#calss header
class _DISTANTLY():
	def __init__(self,): 
		self.name = "DISTANTLY"
		self.definitions = [u'far away: ', u'in an unfriendly way, showing no emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
