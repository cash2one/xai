

#calss header
class _SCRUPULOUS():
	def __init__(self,): 
		self.name = "SCRUPULOUS"
		self.definitions = [u'extremely honest : ', u'doing everything correctly and exactly as it should be done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
