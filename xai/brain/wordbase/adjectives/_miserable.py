

#calss header
class _MISERABLE():
	def __init__(self,): 
		self.name = "MISERABLE"
		self.definitions = [u'very unhappy: ', u'unpleasant and causing unhappiness: ', u'used to emphasize the low quality of value of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
