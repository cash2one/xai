

#calss header
class _UPPERMOST():
	def __init__(self,): 
		self.name = "UPPERMOST"
		self.definitions = [u'in the highest position or having the most importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
