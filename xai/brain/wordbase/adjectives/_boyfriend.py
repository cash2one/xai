

#calss header
class _BOYFRIEND():
	def __init__(self,): 
		self.name = "BOYFRIEND"
		self.definitions = [u"used to refer to a loose, comfortable style of clothing for women that is based on men's clothes: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
