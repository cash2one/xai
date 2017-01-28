

#calss header
class _ATTEMPTED():
	def __init__(self,): 
		self.name = "ATTEMPTED"
		self.definitions = [u'(of a crime) that someone has tried to commit without success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
