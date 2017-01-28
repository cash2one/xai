

#calss header
class _AMBIVALENT():
	def __init__(self,): 
		self.name = "AMBIVALENT"
		self.definitions = [u'having two opposing feelings at the same time, or being uncertain about how you feel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
