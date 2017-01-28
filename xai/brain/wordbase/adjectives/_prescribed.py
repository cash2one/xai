

#calss header
class _PRESCRIBED():
	def __init__(self,): 
		self.name = "PRESCRIBED"
		self.definitions = [u'set by a rule or order: ', u'decided by a doctor as treatment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
