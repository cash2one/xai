

#calss header
class _BALLPARK():
	def __init__(self,): 
		self.name = "BALLPARK"
		self.definitions = [u'A ballpark estimate or figure is a number that is a guess, but one that you believe is near the correct number: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
