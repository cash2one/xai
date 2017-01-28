

#calss header
class _MARKETABLE():
	def __init__(self,): 
		self.name = "MARKETABLE"
		self.definitions = [u'Marketable products or skills are easy to sell because a lot of people want them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
