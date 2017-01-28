

#calss header
class _BERSERK():
	def __init__(self,): 
		self.name = "BERSERK"
		self.definitions = [u'very angry or out of control: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
