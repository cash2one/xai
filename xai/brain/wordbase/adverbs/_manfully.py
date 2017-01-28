

#calss header
class _MANFULLY():
	def __init__(self,): 
		self.name = "MANFULLY"
		self.definitions = [u'with determination and courage, despite great problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
