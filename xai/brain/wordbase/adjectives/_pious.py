

#calss header
class _PIOUS():
	def __init__(self,): 
		self.name = "PIOUS"
		self.definitions = [u'strongly believing in religion, and living in a way that shows this belief: ', u'pretending to have sincere feelings: ', u'something that is unlikely to happen']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
