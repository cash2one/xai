

#calss header
class _LEONINE():
	def __init__(self,): 
		self.name = "LEONINE"
		self.definitions = [u"(often of a person's head or hair) like a lion"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
