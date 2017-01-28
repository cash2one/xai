

#calss header
class _TIMELY():
	def __init__(self,): 
		self.name = "TIMELY"
		self.definitions = [u'happening at the best possible moment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
