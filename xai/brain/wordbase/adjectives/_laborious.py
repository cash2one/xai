

#calss header
class _LABORIOUS():
	def __init__(self,): 
		self.name = "LABORIOUS"
		self.definitions = [u'needing a lot of time and effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
