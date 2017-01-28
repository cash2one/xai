

#calss header
class _IMMODERATE():
	def __init__(self,): 
		self.name = "IMMODERATE"
		self.definitions = [u'too much or many, or more than is usual or reasonable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
