

#calss header
class _HYPNOTIC():
	def __init__(self,): 
		self.name = "HYPNOTIC"
		self.definitions = [u'caused by hypnosis: ', u'Hypnotic sounds or movements are very regular and make you feel as if you want to sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
