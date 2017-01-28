

#calss header
class _ALARMING():
	def __init__(self,): 
		self.name = "ALARMING"
		self.definitions = [u'causing worry or fear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
