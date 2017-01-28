

#calss header
class _RANK():
	def __init__(self,): 
		self.name = "RANK"
		self.definitions = [u'(especially of something bad) complete or extreme: ', u'used to describe plants that grow too fast or too thickly, or an area covered by these: ', u'smelling strong and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
