

#calss header
class _CREAKY():
	def __init__(self,): 
		self.name = "CREAKY"
		self.definitions = [u'Something that is creaky creaks: ', u'used to describe something that is old-fashioned and not now effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
