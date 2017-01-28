

#calss header
class _HAUNTED():
	def __init__(self,): 
		self.name = "HAUNTED"
		self.definitions = [u'showing signs of suffering or severe anxiety: ', u'A haunted place is one where ghosts often appear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
