

#calss header
class _CORRECT():
	def __init__(self,): 
		self.name = "CORRECT"
		self.definitions = [u'in agreement with the true facts or with what is generally accepted: ', u'taking or showing great care to behave or speak in a way that is generally accepted and approved of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
