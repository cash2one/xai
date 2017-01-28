

#calss header
class _INQUIRING():
	def __init__(self,): 
		self.name = "INQUIRING"
		self.definitions = [u"(of someone's behaviour) always wanting to learn new things, or (of someone's expression) wanting to know something: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
