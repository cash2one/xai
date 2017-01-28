

#calss header
class _RUSTY():
	def __init__(self,): 
		self.name = "RUSTY"
		self.definitions = [u'covered with rust (= metal decay): ', u'If a skill you had is rusty, it is not as good as it was because you have not it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
