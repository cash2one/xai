

#calss header
class _HUMANITARIAN():
	def __init__(self,): 
		self.name = "HUMANITARIAN"
		self.definitions = [u"(a person who is) involved in or connected with improving people's lives and reducing suffering: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
