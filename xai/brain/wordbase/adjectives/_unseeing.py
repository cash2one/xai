

#calss header
class _UNSEEING():
	def __init__(self,): 
		self.name = "UNSEEING"
		self.definitions = [u'(especially of eyes) not seeing or noticing anything, although able to see: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
