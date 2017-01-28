

#calss header
class _UNFIT():
	def __init__(self,): 
		self.name = "UNFIT"
		self.definitions = [u'not suitable or good enough for a particular purpose or activity: ', u'not healthy because you do too little exercise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
