

#calss header
class _MOUNTING():
	def __init__(self,): 
		self.name = "MOUNTING"
		self.definitions = [u'gradually increasing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
