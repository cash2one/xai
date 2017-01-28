

#calss header
class _METICULOUS():
	def __init__(self,): 
		self.name = "METICULOUS"
		self.definitions = [u'very careful and with great attention to every detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
