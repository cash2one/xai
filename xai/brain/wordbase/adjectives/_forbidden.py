

#calss header
class _FORBIDDEN():
	def __init__(self,): 
		self.name = "FORBIDDEN"
		self.definitions = [u'not allowed, especially by law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
