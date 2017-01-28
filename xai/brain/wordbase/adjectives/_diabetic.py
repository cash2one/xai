

#calss header
class _DIABETIC():
	def __init__(self,): 
		self.name = "DIABETIC"
		self.definitions = [u'relating to diabetes: ', u'made for diabetic people to eat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
