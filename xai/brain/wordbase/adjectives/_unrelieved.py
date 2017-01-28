

#calss header
class _UNRELIEVED():
	def __init__(self,): 
		self.name = "UNRELIEVED"
		self.definitions = [u'When a bad situation or emotion is unrelieved, it is continuous and never improves, not even for a short period: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
