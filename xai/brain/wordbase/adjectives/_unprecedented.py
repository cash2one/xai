

#calss header
class _UNPRECEDENTED():
	def __init__(self,): 
		self.name = "UNPRECEDENTED"
		self.definitions = [u'never having happened or existed in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
