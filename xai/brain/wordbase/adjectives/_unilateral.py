

#calss header
class _UNILATERAL():
	def __init__(self,): 
		self.name = "UNILATERAL"
		self.definitions = [u'involving only one group or country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
