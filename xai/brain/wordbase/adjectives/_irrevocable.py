

#calss header
class _IRREVOCABLE():
	def __init__(self,): 
		self.name = "IRREVOCABLE"
		self.definitions = [u'impossible to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
