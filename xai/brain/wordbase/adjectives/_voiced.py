

#calss header
class _VOICED():
	def __init__(self,): 
		self.name = "VOICED"
		self.definitions = [u'(of a speech sound) produced by making the vocal cords move very quickly several times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
