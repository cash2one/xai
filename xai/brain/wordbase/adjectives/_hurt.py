

#calss header
class _HURT():
	def __init__(self,): 
		self.name = "HURT"
		self.definitions = [u'injured or in pain: ', u'upset or unhappy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
