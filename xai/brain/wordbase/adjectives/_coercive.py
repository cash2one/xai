

#calss header
class _COERCIVE():
	def __init__(self,): 
		self.name = "COERCIVE"
		self.definitions = [u'using force to persuade people to do things that they are unwilling to do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
