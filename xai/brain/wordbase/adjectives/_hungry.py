

#calss header
class _HUNGRY():
	def __init__(self,): 
		self.name = "HUNGRY"
		self.definitions = [u'wanting or needing food: ', u'having a strong wish or desire for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
