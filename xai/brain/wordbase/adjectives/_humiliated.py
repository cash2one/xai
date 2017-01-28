

#calss header
class _HUMILIATED():
	def __init__(self,): 
		self.name = "HUMILIATED"
		self.definitions = [u'If someone is humiliated, they have has been made to feel ashamed or stupid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
