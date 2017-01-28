

#calss header
class _PUNISHABLE():
	def __init__(self,): 
		self.name = "PUNISHABLE"
		self.definitions = [u'A punishable crime is one that someone can be punished for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
