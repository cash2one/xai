

#calss header
class _PULLOUT():
	def __init__(self,): 
		self.name = "PULLOUT"
		self.definitions = [u'a piece of furniture that can be pulled into position when you want to use it and folded away when you do not']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
