

#calss header
class _ICONOCLASTIC():
	def __init__(self,): 
		self.name = "ICONOCLASTIC"
		self.definitions = [u'strongly opposing generally accepted beliefs and traditions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
