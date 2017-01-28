

#calss header
class _PROLIX():
	def __init__(self,): 
		self.name = "PROLIX"
		self.definitions = [u'using too many words and therefore boring or difficult to read or listen to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
