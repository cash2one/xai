

#calss header
class _FORMER():
	def __init__(self,): 
		self.name = "FORMER"
		self.definitions = [u'of or in an earlier time; before the present time or in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
