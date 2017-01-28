

#calss header
class _SNAZZY():
	def __init__(self,): 
		self.name = "SNAZZY"
		self.definitions = [u'modern and stylish in a way that attracts attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
