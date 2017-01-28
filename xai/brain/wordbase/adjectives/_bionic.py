

#calss header
class _BIONIC():
	def __init__(self,): 
		self.name = "BIONIC"
		self.definitions = [u'using artificial materials and methods to produce activity or movement in a person or animal: ', u'used to refer to a person who has greater powers of strength, speed, etc. than seem to be possible for a human: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
