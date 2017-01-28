

#calss header
class _UNDOUBTED():
	def __init__(self,): 
		self.name = "UNDOUBTED"
		self.definitions = [u'used to emphasize that something is true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
