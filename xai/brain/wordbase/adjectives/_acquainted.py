

#calss header
class _ACQUAINTED():
	def __init__(self,): 
		self.name = "ACQUAINTED"
		self.definitions = [u'knowing or being familiar with a person: ', u'to know or be familiar with something, because you have studied it or have experienced it before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
