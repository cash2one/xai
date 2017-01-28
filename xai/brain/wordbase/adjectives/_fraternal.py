

#calss header
class _FRATERNAL():
	def __init__(self,): 
		self.name = "FRATERNAL"
		self.definitions = [u'relating to brothers: ', u'friendly, like brothers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
