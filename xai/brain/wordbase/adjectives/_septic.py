

#calss header
class _SEPTIC():
	def __init__(self,): 
		self.name = "SEPTIC"
		self.definitions = [u'infected by bacteria that produce pus: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
