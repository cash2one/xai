

#calss header
class _CAPABLE():
	def __init__(self,): 
		self.name = "CAPABLE"
		self.definitions = [u'able to do things effectively and skilfully, and to achieve results: ', u'having the ability, power, or qualities to be able to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
