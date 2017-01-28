

#calss header
class _BROAD():
	def __init__(self,): 
		self.name = "BROAD"
		self.definitions = [u'very wide: ', u'If something is a particular distance broad, it measures this distance from side to side: ', u'including a wide range of things; general: ', u'If someone has a broad accent (= way of speaking), it is strong and noticeable, showing where they come from: ', u'a hint (= when you tell someone something without saying it directly) that is easy to understand']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
