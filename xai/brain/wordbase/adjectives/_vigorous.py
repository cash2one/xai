

#calss header
class _VIGOROUS():
	def __init__(self,): 
		self.name = "VIGOROUS"
		self.definitions = [u'very forceful or energetic: ', u'healthy and strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
