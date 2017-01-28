

#calss header
class _PROOF():
	def __init__(self,): 
		self.name = "PROOF"
		self.definitions = [u'of the stated alcoholic strength, a higher number meaning a greater amount of alcohol: ', u'providing protection against something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
