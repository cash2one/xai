

#calss header
class _ASSIDUOUS():
	def __init__(self,): 
		self.name = "ASSIDUOUS"
		self.definitions = [u'showing hard work, care, and attention to detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
