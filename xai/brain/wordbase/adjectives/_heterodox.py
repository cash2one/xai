

#calss header
class _HETERODOX():
	def __init__(self,): 
		self.name = "HETERODOX"
		self.definitions = [u'(of beliefs, ideas, or activities) different to and opposing generally accepted beliefs or standards: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
