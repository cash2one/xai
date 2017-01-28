

#calss header
class _RETARDED():
	def __init__(self,): 
		self.name = "RETARDED"
		self.definitions = [u'having had a slower mental development than other people of the same age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
