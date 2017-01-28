

#calss header
class _SIZABLE():
	def __init__(self,): 
		self.name = "SIZABLE"
		self.definitions = [u'mainly US spelling of  sizeable ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
