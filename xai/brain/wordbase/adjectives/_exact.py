

#calss header
class _EXACT():
	def __init__(self,): 
		self.name = "EXACT"
		self.definitions = [u'in great detail, or complete, correct, or true in every way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
