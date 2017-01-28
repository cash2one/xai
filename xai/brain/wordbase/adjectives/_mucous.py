

#calss header
class _MUCOUS():
	def __init__(self,): 
		self.name = "MUCOUS"
		self.definitions = [u'relating to mucus (= a slippery lubricant and protective substance): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
