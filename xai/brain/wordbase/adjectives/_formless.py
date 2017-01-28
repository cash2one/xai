

#calss header
class _FORMLESS():
	def __init__(self,): 
		self.name = "FORMLESS"
		self.definitions = [u'without clear shape or structure']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
