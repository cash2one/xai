

#calss header
class _RUTHLESS():
	def __init__(self,): 
		self.name = "RUTHLESS"
		self.definitions = [u'not thinking or worrying about any pain caused to others; cruel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
