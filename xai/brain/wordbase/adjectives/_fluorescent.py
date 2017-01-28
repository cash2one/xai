

#calss header
class _FLUORESCENT():
	def __init__(self,): 
		self.name = "FLUORESCENT"
		self.definitions = [u'Fluorescent lights are very bright, tube-shaped electric lights, often used in offices: ', u'Fluorescent colours are very bright and can be seen in the dark: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
