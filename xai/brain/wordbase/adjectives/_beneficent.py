

#calss header
class _BENEFICENT():
	def __init__(self,): 
		self.name = "BENEFICENT"
		self.definitions = [u'helping people and doing good acts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
