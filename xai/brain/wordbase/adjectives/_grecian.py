

#calss header
class _GRECIAN():
	def __init__(self,): 
		self.name = "GRECIAN"
		self.definitions = [u"(especially of building styles or a person's appearance) beautiful and simple, in the style of Ancient Greece: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
