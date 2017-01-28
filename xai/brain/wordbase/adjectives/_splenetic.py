

#calss header
class _SPLENETIC():
	def __init__(self,): 
		self.name = "SPLENETIC"
		self.definitions = [u'used to describe a person who easily becomes angry or annoyed, or their behaviour : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
