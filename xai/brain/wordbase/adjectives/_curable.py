

#calss header
class _CURABLE():
	def __init__(self,): 
		self.name = "CURABLE"
		self.definitions = [u'A curable disease can be cured: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
