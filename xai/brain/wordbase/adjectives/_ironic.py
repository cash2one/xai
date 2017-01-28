

#calss header
class _IRONIC():
	def __init__(self,): 
		self.name = "IRONIC"
		self.definitions = [u'interesting, strange, or funny because of being very different from what you would usually expect: ', u'showing that you really mean the opposite of what you are saying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
