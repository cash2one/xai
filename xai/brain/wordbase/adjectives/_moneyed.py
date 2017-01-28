

#calss header
class _MONEYED():
	def __init__(self,): 
		self.name = "MONEYED"
		self.definitions = [u'rich: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
