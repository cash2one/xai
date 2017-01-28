

#calss header
class _UNSPOILED():
	def __init__(self,): 
		self.name = "UNSPOILED"
		self.definitions = [u'An unspoiled place is beautiful because it has not been changed or damaged by people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
