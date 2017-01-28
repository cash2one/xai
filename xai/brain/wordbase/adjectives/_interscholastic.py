

#calss header
class _INTERSCHOLASTIC():
	def __init__(self,): 
		self.name = "INTERSCHOLASTIC"
		self.definitions = [u'involving two or more schools: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
