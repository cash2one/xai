

#calss header
class _HUMBLE():
	def __init__(self,): 
		self.name = "HUMBLE"
		self.definitions = [u'not proud or not believing that you are important: ', u'poor or of a low social rank: ', u'ordinary; not special or very important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
