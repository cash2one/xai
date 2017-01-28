

#calss header
class _SPIDERY():
	def __init__(self,): 
		self.name = "SPIDERY"
		self.definitions = [u"consisting of thin, dark, bending lines, like a spider's legs: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
