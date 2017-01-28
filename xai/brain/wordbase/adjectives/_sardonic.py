

#calss header
class _SARDONIC():
	def __init__(self,): 
		self.name = "SARDONIC"
		self.definitions = [u'showing little respect in a humorous but unkind way, often because you think that you are too important to consider or discuss a matter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
