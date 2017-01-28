

#calss header
class _SNOWY():
	def __init__(self,): 
		self.name = "SNOWY"
		self.definitions = [u'full of or like snow: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
