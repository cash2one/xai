

#calss header
class _SMACK():
	def __init__(self,): 
		self.name = "SMACK"
		self.definitions = [u'exactly in a place or a situation: ', u'directly and forcefully, producing a short, loud noise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
