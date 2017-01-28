

#calss header
class _PREMENSTRUAL():
	def __init__(self,): 
		self.name = "PREMENSTRUAL"
		self.definitions = [u"of the time just before a woman's period"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
