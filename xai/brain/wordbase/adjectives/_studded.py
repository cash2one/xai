

#calss header
class _STUDDED():
	def __init__(self,): 
		self.name = "STUDDED"
		self.definitions = [u'made with metal studs fixed into the surface in a pattern: ', u'If something is studded with many objects of the same type, those objects are arranged regularly across it, or across the surface of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
