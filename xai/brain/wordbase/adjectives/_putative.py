

#calss header
class _PUTATIVE():
	def __init__(self,): 
		self.name = "PUTATIVE"
		self.definitions = [u'generally thought to be or to exist, even if this may not really be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
