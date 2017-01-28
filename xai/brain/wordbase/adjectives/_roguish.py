

#calss header
class _ROGUISH():
	def __init__(self,): 
		self.name = "ROGUISH"
		self.definitions = [u'(of a person) looking as if they are going to laugh because of slightly bad behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
