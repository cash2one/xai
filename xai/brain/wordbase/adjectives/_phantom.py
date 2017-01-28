

#calss header
class _PHANTOM():
	def __init__(self,): 
		self.name = "PHANTOM"
		self.definitions = [u'like a ghost: ', u'used to describe something that you imagine exists or that appears to exist, although in fact it does not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
