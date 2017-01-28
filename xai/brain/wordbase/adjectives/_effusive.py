

#calss header
class _EFFUSIVE():
	def __init__(self,): 
		self.name = "EFFUSIVE"
		self.definitions = [u'expressing welcome, approval, or pleasure in a way that shows very strong feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
