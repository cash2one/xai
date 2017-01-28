

#calss header
class _PUNCTUAL():
	def __init__(self,): 
		self.name = "PUNCTUAL"
		self.definitions = [u'arriving, doing something, or happening at the expected, correct time; not late: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
