

#calss header
class _DEMOGRAPHIC():
	def __init__(self,): 
		self.name = "DEMOGRAPHIC"
		self.definitions = [u'relating to demography (= the study of populations and the different groups that make them up): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
