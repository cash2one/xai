

#calss header
class _GUILTY():
	def __init__(self,): 
		self.name = "GUILTY"
		self.definitions = [u'feeling guilt: ', u'responsible for breaking a law: ', u'the person who has done something wrong or who has committed a crime']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
