

#calss header
class _INCONTESTABLE():
	def __init__(self,): 
		self.name = "INCONTESTABLE"
		self.definitions = [u'impossible to question because of being obviously true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
