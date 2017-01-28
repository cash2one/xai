

#calss header
class _UNENDURABLE():
	def __init__(self,): 
		self.name = "UNENDURABLE"
		self.definitions = [u'If a situation or experience is unendurable, it is so unpleasant or painful that it is almost impossible to bear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
