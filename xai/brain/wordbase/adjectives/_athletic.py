

#calss header
class _ATHLETIC():
	def __init__(self,): 
		self.name = "ATHLETIC"
		self.definitions = [u'strong, healthy, and good at sports: ', u'relating to athletes or athletics: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
