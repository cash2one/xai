

#calss header
class _EXIGENT():
	def __init__(self,): 
		self.name = "EXIGENT"
		self.definitions = [u'needing urgent attention, or demanding too much from other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
