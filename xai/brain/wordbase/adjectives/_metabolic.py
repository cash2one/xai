

#calss header
class _METABOLIC():
	def __init__(self,): 
		self.name = "METABOLIC"
		self.definitions = [u'relating to metabolism (= the chemical processes within the body required for life): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
