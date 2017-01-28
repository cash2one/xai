

#calss header
class _GLOBAL():
	def __init__(self,): 
		self.name = "GLOBAL"
		self.definitions = [u'relating to the whole world: ', u'considering or relating to all parts of a situation or subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
