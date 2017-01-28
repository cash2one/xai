

#calss header
class _REFLEXIVELY():
	def __init__(self,): 
		self.name = "REFLEXIVELY"
		self.definitions = [u'in a way that is caused by an uncontrolled physical reaction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
