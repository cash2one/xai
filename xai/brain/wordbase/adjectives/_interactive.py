

#calss header
class _INTERACTIVE():
	def __init__(self,): 
		self.name = "INTERACTIVE"
		self.definitions = [u'An interactive system or computer program is designed to involve the user in the exchange of information: ', u'involving communication between people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
