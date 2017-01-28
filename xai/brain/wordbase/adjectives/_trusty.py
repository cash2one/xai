

#calss header
class _TRUSTY():
	def __init__(self,): 
		self.name = "TRUSTY"
		self.definitions = [u'able to be trusted, especially because of having been owned and used for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
