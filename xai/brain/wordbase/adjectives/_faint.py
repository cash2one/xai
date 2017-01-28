

#calss header
class _FAINT():
	def __init__(self,): 
		self.name = "FAINT"
		self.definitions = [u'not strong or clear; slight: ', u'used to emphasize that you do not know something: ', u'to feel weak, as if you are about to become unconscious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
