

#calss header
class _MISANTHROPIC():
	def __init__(self,): 
		self.name = "MISANTHROPIC"
		self.definitions = [u'not liking other people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
