

#calss header
class _AGREED():
	def __init__(self,): 
		self.name = "AGREED"
		self.definitions = [u'accepted: ', u'If two or more people are agreed, they have the same opinion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
