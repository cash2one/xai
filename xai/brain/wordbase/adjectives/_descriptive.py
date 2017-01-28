

#calss header
class _DESCRIPTIVE():
	def __init__(self,): 
		self.name = "DESCRIPTIVE"
		self.definitions = [u'describing something, especially in a detailed, interesting way: ', u'A descriptive area of study is one that is based on saying what its subject is really like, rather than on developing theories about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
