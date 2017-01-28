

#calss header
class _OPERATIONAL():
	def __init__(self,): 
		self.name = "OPERATIONAL"
		self.definitions = [u'relating to a particular activity: ', u'If a system is operational, it is working: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
