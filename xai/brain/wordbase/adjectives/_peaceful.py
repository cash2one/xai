

#calss header
class _PEACEFUL():
	def __init__(self,): 
		self.name = "PEACEFUL"
		self.definitions = [u'without violence: ', u'quiet and calm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
