

#calss header
class _DISORDERLY():
	def __init__(self,): 
		self.name = "DISORDERLY"
		self.definitions = [u'untidy and badly organized: ', u'angry and violent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
