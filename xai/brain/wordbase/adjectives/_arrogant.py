

#calss header
class _ARROGANT():
	def __init__(self,): 
		self.name = "ARROGANT"
		self.definitions = [u'unpleasantly proud and behaving as if you are more important than, or know more than, other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
