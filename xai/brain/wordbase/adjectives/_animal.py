

#calss header
class _ANIMAL():
	def __init__(self,): 
		self.name = "ANIMAL"
		self.definitions = [u'made or obtained from an animal or animals: ', u'relating to, or taking the form of, an animal or animals rather than a plant or human being: ', u'relating to physical desires or needs, and not spiritual or mental ones: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
