

#calss header
class _CAUCASIAN():
	def __init__(self,): 
		self.name = "CAUCASIAN"
		self.definitions = [u'belonging to the races of people who have skin that is of a pale colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
