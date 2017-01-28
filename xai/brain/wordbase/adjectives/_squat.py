

#calss header
class _SQUAT():
	def __init__(self,): 
		self.name = "SQUAT"
		self.definitions = [u'short and wide, usually in a way that is not attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
