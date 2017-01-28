

#calss header
class _COLOUR():
	def __init__(self,): 
		self.name = "COLOUR"
		self.definitions = [u'Colour television, photography, or printing shows things in all their colours, not just in black and white.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
