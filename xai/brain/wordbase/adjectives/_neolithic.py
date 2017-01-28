

#calss header
class _NEOLITHIC():
	def __init__(self,): 
		self.name = "NEOLITHIC"
		self.definitions = [u'relating to the period when humans used tools and weapons made of stone and had just developed farming: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
