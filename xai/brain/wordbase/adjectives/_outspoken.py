

#calss header
class _OUTSPOKEN():
	def __init__(self,): 
		self.name = "OUTSPOKEN"
		self.definitions = [u'expressing strong opinions very directly without worrying if other people are offended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
