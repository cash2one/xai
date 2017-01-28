

#calss header
class _PROFANE():
	def __init__(self,): 
		self.name = "PROFANE"
		self.definitions = [u'showing no respect for a god or a religion, often through language: ', u'not relating to religion or spiritual matters: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
