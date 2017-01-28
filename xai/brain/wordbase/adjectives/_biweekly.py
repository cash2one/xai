

#calss header
class _BIWEEKLY():
	def __init__(self,): 
		self.name = "BIWEEKLY"
		self.definitions = [u'happening or appearing every two weeks or twice a week: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
