

#calss header
class _WAN():
	def __init__(self,): 
		self.name = "WAN"
		self.definitions = [u"(of a person's face) more pale than usual and tired-looking"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
