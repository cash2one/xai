

#calss header
class _WRETCHED():
	def __init__(self,): 
		self.name = "WRETCHED"
		self.definitions = [u'unpleasant or of low quality: ', u'very ill or very unhappy: ', u'used to express anger when something annoying happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
