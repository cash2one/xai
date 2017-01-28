

#calss header
class _BLAND():
	def __init__(self,): 
		self.name = "BLAND"
		self.definitions = [u'not having a strong taste or character or not showing any interest or energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
