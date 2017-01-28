

#calss header
class _NOTABLE():
	def __init__(self,): 
		self.name = "NOTABLE"
		self.definitions = [u'important and deserving attention, because of being very good or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
