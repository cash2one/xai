

#calss header
class _WINDWARD():
	def __init__(self,): 
		self.name = "WINDWARD"
		self.definitions = [u'(on the side of a hill, etc.) facing the wind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
