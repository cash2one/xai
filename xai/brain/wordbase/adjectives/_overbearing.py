

#calss header
class _OVERBEARING():
	def __init__(self,): 
		self.name = "OVERBEARING"
		self.definitions = [u'too confident and too determined to tell other people what to do, in a way that is unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
