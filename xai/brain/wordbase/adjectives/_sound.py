

#calss header
class _SOUND():
	def __init__(self,): 
		self.name = "SOUND"
		self.definitions = [u'not broken or damaged; healthy; in good condition: ', u'showing good judgment; able to be trusted: ', u'complete: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
