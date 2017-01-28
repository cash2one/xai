

#calss header
class _BEAMING():
	def __init__(self,): 
		self.name = "BEAMING"
		self.definitions = [u'used to describe a smile that is very wide and happy, or someone who is smiling in this way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
