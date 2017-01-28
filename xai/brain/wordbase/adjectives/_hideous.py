

#calss header
class _HIDEOUS():
	def __init__(self,): 
		self.name = "HIDEOUS"
		self.definitions = [u'extremely ugly or bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
