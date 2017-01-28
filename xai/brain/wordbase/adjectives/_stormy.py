

#calss header
class _STORMY():
	def __init__(self,): 
		self.name = "STORMY"
		self.definitions = [u'with strong wind, heavy rain, and often thunder and lightning: ', u'involving a lot of strong argument and shouting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
