

#calss header
class _FADDISH():
	def __init__(self,): 
		self.name = "FADDISH"
		self.definitions = [u'fashionable but not likely to stay fashionable for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
