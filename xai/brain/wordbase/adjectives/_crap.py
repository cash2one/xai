

#calss header
class _CRAP():
	def __init__(self,): 
		self.name = "CRAP"
		self.definitions = [u'of very bad quality: ', u'not skilled or not organized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
