

#calss header
class _WINDED():
	def __init__(self,): 
		self.name = "WINDED"
		self.definitions = [u'temporarily unable to breathe, either when hit in the stomach or after taking hard physical exercise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
