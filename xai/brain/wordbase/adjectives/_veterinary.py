

#calss header
class _VETERINARY():
	def __init__(self,): 
		self.name = "VETERINARY"
		self.definitions = [u'connected with taking care of the health of animals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
