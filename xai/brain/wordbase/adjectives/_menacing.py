

#calss header
class _MENACING():
	def __init__(self,): 
		self.name = "MENACING"
		self.definitions = [u'making you think that someone is going to do something bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
