

#calss header
class _STRENUOUS():
	def __init__(self,): 
		self.name = "STRENUOUS"
		self.definitions = [u'needing or using a lot of physical or mental effort or energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
