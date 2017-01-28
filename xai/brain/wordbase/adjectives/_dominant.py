

#calss header
class _DOMINANT():
	def __init__(self,): 
		self.name = "DOMINANT"
		self.definitions = [u'more important, strong, or noticeable than anything else of the same type: ', u'A dominant gene is one that always produces a particular characteristic in a person, plant, or animal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
