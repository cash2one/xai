

#calss header
class _DISPOSED():
	def __init__(self,): 
		self.name = "DISPOSED"
		self.definitions = [u'to be willing or likely to do something: ', u'to like or approve of something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
