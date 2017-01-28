

#calss header
class _HORMONAL():
	def __init__(self,): 
		self.name = "HORMONAL"
		self.definitions = [u'relating to hormones: ', u'feeling the effect of hormones, especially when this makes your emotions stronger or more likely to change than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
