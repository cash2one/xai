

#calss header
class _POIGNANT():
	def __init__(self,): 
		self.name = "POIGNANT"
		self.definitions = [u'causing or having a very sharp feeling of sadness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
