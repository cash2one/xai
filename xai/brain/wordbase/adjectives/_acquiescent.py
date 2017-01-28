

#calss header
class _ACQUIESCENT():
	def __init__(self,): 
		self.name = "ACQUIESCENT"
		self.definitions = [u'willing to do what other people want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
