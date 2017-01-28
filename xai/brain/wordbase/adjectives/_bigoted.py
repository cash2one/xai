

#calss header
class _BIGOTED():
	def __init__(self,): 
		self.name = "BIGOTED"
		self.definitions = [u'having strong, unreasonable beliefs and disliking other people who have different beliefs or a different way of life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
