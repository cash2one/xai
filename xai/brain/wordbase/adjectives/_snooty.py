

#calss header
class _SNOOTY():
	def __init__(self,): 
		self.name = "SNOOTY"
		self.definitions = [u'behaving in an unfriendly way because you believe you are better than other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
