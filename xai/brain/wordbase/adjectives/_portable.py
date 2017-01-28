

#calss header
class _PORTABLE():
	def __init__(self,): 
		self.name = "PORTABLE"
		self.definitions = [u'light and small enough to be easily carried or moved: ', u'possible to take with you if you move to a different place or job: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
