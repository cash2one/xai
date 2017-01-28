

#calss header
class _DAZZLING():
	def __init__(self,): 
		self.name = "DAZZLING"
		self.definitions = [u'A dazzling light is so bright that you cannot see for a short time after looking at it: ', u'extremely attractive or exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
