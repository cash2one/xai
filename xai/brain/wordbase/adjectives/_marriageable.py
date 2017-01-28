

#calss header
class _MARRIAGEABLE():
	def __init__(self,): 
		self.name = "MARRIAGEABLE"
		self.definitions = [u'suitable for marriage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
