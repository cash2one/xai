

#calss header
class _SPORTSMANLIKE():
	def __init__(self,): 
		self.name = "SPORTSMANLIKE"
		self.definitions = [u'behaving in a way that is fair and shows respect towards the other players when playing sport']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
