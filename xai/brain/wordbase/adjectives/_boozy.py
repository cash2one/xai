

#calss header
class _BOOZY():
	def __init__(self,): 
		self.name = "BOOZY"
		self.definitions = [u'drinking or containing a lot of alcohol: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
