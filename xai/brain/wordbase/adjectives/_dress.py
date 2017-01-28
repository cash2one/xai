

#calss header
class _DRESS():
	def __init__(self,): 
		self.name = "DRESS"
		self.definitions = [u"used to refer to men's suits, shirts, or other clothes of the type that are worn at formal occasions: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
