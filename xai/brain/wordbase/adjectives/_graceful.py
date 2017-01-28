

#calss header
class _GRACEFUL():
	def __init__(self,): 
		self.name = "GRACEFUL"
		self.definitions = [u'moving in a smooth, relaxed, attractive way, or having a smooth, attractive shape: ', u'behaving in a polite and pleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
