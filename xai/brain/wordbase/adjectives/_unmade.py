

#calss header
class _UNMADE():
	def __init__(self,): 
		self.name = "UNMADE"
		self.definitions = [u'If a bed is unmade, its sheets and covers are still untidy from having been slept in.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
