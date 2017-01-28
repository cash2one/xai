

#calss header
class _SHORTISH():
	def __init__(self,): 
		self.name = "SHORTISH"
		self.definitions = [u'fairly short: ', u'not long, but not very short: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
