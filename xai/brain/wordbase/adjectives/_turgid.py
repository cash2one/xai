

#calss header
class _TURGID():
	def __init__(self,): 
		self.name = "TURGID"
		self.definitions = [u'(of speech, writing, style, etc.) too serious about its subject matter; boring: ', u'(of water) not flowing easily: ', u'(of an organ or living tissue) swollen']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
