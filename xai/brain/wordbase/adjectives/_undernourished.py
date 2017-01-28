

#calss header
class _UNDERNOURISHED():
	def __init__(self,): 
		self.name = "UNDERNOURISHED"
		self.definitions = [u'not eating enough food to continue to be in good health: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
