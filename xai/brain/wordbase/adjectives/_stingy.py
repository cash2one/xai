

#calss header
class _STINGY():
	def __init__(self,): 
		self.name = "STINGY"
		self.definitions = [u'unwilling to spend money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
