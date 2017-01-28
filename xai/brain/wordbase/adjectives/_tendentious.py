

#calss header
class _TENDENTIOUS():
	def __init__(self,): 
		self.name = "TENDENTIOUS"
		self.definitions = [u'(of speech or writing) expressing or supporting a particular opinion that many other people disagree with']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
