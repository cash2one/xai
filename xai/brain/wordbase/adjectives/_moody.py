

#calss header
class _MOODY():
	def __init__(self,): 
		self.name = "MOODY"
		self.definitions = [u'If someone is moody, their moods change suddenly and they become angry or unhappy easily: ', u'expressing something mysterious or slightly sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
