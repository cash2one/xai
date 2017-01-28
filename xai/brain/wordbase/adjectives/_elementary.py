

#calss header
class _ELEMENTARY():
	def __init__(self,): 
		self.name = "ELEMENTARY"
		self.definitions = [u'basic: ', u'relating to the early stages of studying a subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
