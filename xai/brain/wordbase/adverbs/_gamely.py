

#calss header
class _GAMELY():
	def __init__(self,): 
		self.name = "GAMELY"
		self.definitions = [u'in a way that shows you are willing to do something new, difficult, or that involves risks; bravely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
