

#calss header
class _SALEABLE():
	def __init__(self,): 
		self.name = "SALEABLE"
		self.definitions = [u'easy to sell or suitable for selling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
