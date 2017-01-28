

#calss header
class _INSCRUTABLE():
	def __init__(self,): 
		self.name = "INSCRUTABLE"
		self.definitions = [u'not showing emotions or thoughts and therefore very difficult to understand or get to know: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
