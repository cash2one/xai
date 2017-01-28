

#calss header
class _TECHNICAL():
	def __init__(self,): 
		self.name = "TECHNICAL"
		self.definitions = [u'relating to the knowledge, machines, or methods used in science and industry: ', u'relating to the knowledge and methods of a particular subject or job: ', u'relating to practical skills and methods that are used in a particular activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
