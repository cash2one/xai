

#calss header
class _GOURMET():
	def __init__(self,): 
		self.name = "GOURMET"
		self.definitions = [u'(of food) very high quality: ', u'producing or serving food that is very high quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
