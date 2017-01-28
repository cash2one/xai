

#calss header
class _COMMODIOUS():
	def __init__(self,): 
		self.name = "COMMODIOUS"
		self.definitions = [u'used to describe a room or house that has a lot of space']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
