

#calss header
class _DOUR():
	def __init__(self,): 
		self.name = "DOUR"
		self.definitions = [u"(usually of a person's appearance or manner) unfriendly, unhappy, and very serious: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
