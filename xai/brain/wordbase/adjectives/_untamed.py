

#calss header
class _UNTAMED():
	def __init__(self,): 
		self.name = "UNTAMED"
		self.definitions = [u'left in a natural or wild state: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
