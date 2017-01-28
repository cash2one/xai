

#calss header
class _HEARTFELT():
	def __init__(self,): 
		self.name = "HEARTFELT"
		self.definitions = [u'strongly felt and sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
