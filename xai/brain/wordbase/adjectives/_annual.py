

#calss header
class _ANNUAL():
	def __init__(self,): 
		self.name = "ANNUAL"
		self.definitions = [u'happening once every year: ', u'relating to a period of one year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
