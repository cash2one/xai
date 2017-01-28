

#calss header
class _FRACTIONAL():
	def __init__(self,): 
		self.name = "FRACTIONAL"
		self.definitions = [u'extremely small: ', u'relating to only a part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
