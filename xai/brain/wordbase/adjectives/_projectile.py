

#calss header
class _PROJECTILE():
	def __init__(self,): 
		self.name = "PROJECTILE"
		self.definitions = [u'used to describe things that are thrown or shot forwards with great force: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
