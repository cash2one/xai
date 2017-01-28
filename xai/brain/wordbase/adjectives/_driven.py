

#calss header
class _DRIVEN():
	def __init__(self,): 
		self.name = "DRIVEN"
		self.definitions = [u'Someone who is driven is so determined to achieve something or be successful that all of their behaviour is directed towards this aim: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
