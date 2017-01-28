

#calss header
class _INDIGNANT():
	def __init__(self,): 
		self.name = "INDIGNANT"
		self.definitions = [u'angry because of something that is wrong or not fair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
