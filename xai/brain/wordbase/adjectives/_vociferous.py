

#calss header
class _VOCIFEROUS():
	def __init__(self,): 
		self.name = "VOCIFEROUS"
		self.definitions = [u'Vociferous people express their opinions and complaints loudly and repeatedly in speech, and vociferous demands, etc. are made repeatedly and loudly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
