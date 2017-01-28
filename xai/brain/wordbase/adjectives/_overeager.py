

#calss header
class _OVEREAGER():
	def __init__(self,): 
		self.name = "OVEREAGER"
		self.definitions = [u'too eager: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
