

#calss header
class _YESTERDAY():
	def __init__(self,): 
		self.name = "YESTERDAY"
		self.definitions = [u'on the day before today: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
