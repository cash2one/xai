

#calss header
class _HOMESICK():
	def __init__(self,): 
		self.name = "HOMESICK"
		self.definitions = [u'unhappy because of being away from home for a long period: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
