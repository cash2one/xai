

#calss header
class _DAPPER():
	def __init__(self,): 
		self.name = "DAPPER"
		self.definitions = [u'A dapper man is dressed in a fashionable and tidy way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
