

#calss header
class _COPTIC():
	def __init__(self,): 
		self.name = "COPTIC"
		self.definitions = [u'of or connected with the ancient Christian Church of Egypt, now based in Egypt and Ethiopia: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
