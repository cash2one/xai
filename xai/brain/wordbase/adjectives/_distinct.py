

#calss header
class _DISTINCT():
	def __init__(self,): 
		self.name = "DISTINCT"
		self.definitions = [u'clearly noticeable; that certainly exists: ', u'clearly separate and different (from something else): ', u'rather than: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
