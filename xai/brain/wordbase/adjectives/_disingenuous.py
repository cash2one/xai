

#calss header
class _DISINGENUOUS():
	def __init__(self,): 
		self.name = "DISINGENUOUS"
		self.definitions = [u'(of a person or their behaviour) slightly dishonest, or not speaking the complete truth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
