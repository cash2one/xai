

#calss header
class _HYPODERMIC():
	def __init__(self,): 
		self.name = "HYPODERMIC"
		self.definitions = [u"(of medical tools) used to inject drugs (= put them into the body) under a person's skin: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
