

#calss header
class _CONFUSING():
	def __init__(self,): 
		self.name = "CONFUSING"
		self.definitions = [u'Something that is confusing makes you feel confused because it is difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
