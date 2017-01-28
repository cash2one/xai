

#calss header
class _UPHILL():
	def __init__(self,): 
		self.name = "UPHILL"
		self.definitions = [u'leading to a higher place on a slope: ', u'needing a large amount of effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
