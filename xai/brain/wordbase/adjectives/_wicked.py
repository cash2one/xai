

#calss header
class _WICKED():
	def __init__(self,): 
		self.name = "WICKED"
		self.definitions = [u'morally wrong and bad: ', u'slightly immoral or bad for you, but in an attractive way: ', u'excellent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
