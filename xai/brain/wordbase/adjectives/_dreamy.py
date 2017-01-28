

#calss header
class _DREAMY():
	def __init__(self,): 
		self.name = "DREAMY"
		self.definitions = [u'seeming to be in a dream and not paying attention to what is happening around you: ', u'very pleasant or attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
