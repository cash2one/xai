

#calss header
class _UNRECORDED():
	def __init__(self,): 
		self.name = "UNRECORDED"
		self.definitions = [u'not written about before, and therefore not known about: ', u'(of sounds or moving pictures) not recorded on electronic equipment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
