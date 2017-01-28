

#calss header
class _INSATIABLE():
	def __init__(self,): 
		self.name = "INSATIABLE"
		self.definitions = [u'(especially of a desire or need) too great to be satisfied: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
