

#calss header
class _PREPARED():
	def __init__(self,): 
		self.name = "PREPARED"
		self.definitions = [u'ready to deal with a situation: ', u'made earlier: ', u'to be willing, or happy to agree to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
