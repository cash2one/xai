

#calss header
class _COMFY():
	def __init__(self,): 
		self.name = "COMFY"
		self.definitions = [u'informal for comfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
