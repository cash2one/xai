

#calss header
class _PUZZLED():
	def __init__(self,): 
		self.name = "PUZZLED"
		self.definitions = [u'confused because you do not understand something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
