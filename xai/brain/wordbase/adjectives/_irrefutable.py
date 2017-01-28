

#calss header
class _IRREFUTABLE():
	def __init__(self,): 
		self.name = "IRREFUTABLE"
		self.definitions = [u'impossible to prove wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
