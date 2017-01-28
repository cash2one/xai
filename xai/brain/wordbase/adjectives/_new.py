

#calss header
class _NEW():
	def __init__(self,): 
		self.name = "NEW"
		self.definitions = [u'recently created or having started to exist recently: ', u'different from one that existed earlier: ', u'not yet familiar or experienced: ', u'not previously used or owned: ', u'recently discovered or made known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
