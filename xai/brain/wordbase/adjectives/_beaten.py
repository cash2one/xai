

#calss header
class _BEATEN():
	def __init__(self,): 
		self.name = "BEATEN"
		self.definitions = [u'Beaten gold or another metal has been made flat by having been hit repeatedly with a hard object: ', u'A beaten path or track is one that people walk along regularly so that the ground has become hard and the path is clear.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
