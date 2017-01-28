

#calss header
class _VICTORIAN():
	def __init__(self,): 
		self.name = "VICTORIAN"
		self.definitions = [u'belonging to, made in, or living in the time when Queen Victoria was queen of Great Britain and Ireland (1837\u20131901): ', u'Victorian ideas, beliefs, etc. are ones considered to be typical of the time when Queen Victoria was queen, such as a belief in strict moral and religious rules and in the importance of family life: ', u'from or belonging or relating to the state of Victoria']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
