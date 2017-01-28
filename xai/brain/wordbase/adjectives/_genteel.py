

#calss header
class _GENTEEL():
	def __init__(self,): 
		self.name = "GENTEEL"
		self.definitions = [u'typical of a high social class: ', u'being very polite, gentle, or graceful: ', u'calm and gentle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
