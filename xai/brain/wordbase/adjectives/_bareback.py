

#calss header
class _BAREBACK():
	def __init__(self,): 
		self.name = "BAREBACK"
		self.definitions = [u'without a saddle on the back of a horse that is being ridden: ', u'(of sexual activity) performed without using a condom']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
