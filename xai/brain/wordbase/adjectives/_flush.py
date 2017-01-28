

#calss header
class _FLUSH():
	def __init__(self,): 
		self.name = "FLUSH"
		self.definitions = [u'at the same level as another surface: ', u'having a lot of money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
