

#calss header
class _STILTED():
	def __init__(self,): 
		self.name = "STILTED"
		self.definitions = [u"(of a person's behaviour or way of speaking or writing) too formal and not smooth or natural: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
