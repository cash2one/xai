

#calss header
class _VIBRANT():
	def __init__(self,): 
		self.name = "VIBRANT"
		self.definitions = [u'energetic, exciting, and full of enthusiasm: ', u'Vibrant colour or light is bright and strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
