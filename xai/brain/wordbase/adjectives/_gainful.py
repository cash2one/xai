

#calss header
class _GAINFUL():
	def __init__(self,): 
		self.name = "GAINFUL"
		self.definitions = [u'providing money or something else that is useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
