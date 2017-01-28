

#calss header
class _CLOVEN():
	def __init__(self,): 
		self.name = "CLOVEN"
		self.definitions = [u"used to describe something, especially an animal's hoof, that is divided into two parts: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
