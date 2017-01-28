

#calss header
class _OFFHAND():
	def __init__(self,): 
		self.name = "OFFHAND"
		self.definitions = [u'not friendly, and showing little interest in other people in a way that seems slightly rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
