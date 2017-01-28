

#calss header
class _TACTILE():
	def __init__(self,): 
		self.name = "TACTILE"
		self.definitions = [u'related to the sense of touch', u'If something is tactile, it has a surface that is pleasant or attractive to touch: ', u'A tactile person touches other people a lot.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
