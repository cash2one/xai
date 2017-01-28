

#calss header
class _GRUFF():
	def __init__(self,): 
		self.name = "GRUFF"
		self.definitions = [u"(of a person's voice) low and unfriendly, or (of a person's behaviour) unfriendly or showing no patience: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
