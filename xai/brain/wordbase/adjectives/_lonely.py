

#calss header
class _LONELY():
	def __init__(self,): 
		self.name = "LONELY"
		self.definitions = [u'unhappy because you are not with other people: ', u'A lonely place is a long way from where people live: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
