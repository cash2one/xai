

#calss header
class _ENCLOSED():
	def __init__(self,): 
		self.name = "ENCLOSED"
		self.definitions = [u'surrounded by walls, objects, or structures: ', u'sent to someone in an envelope with a letter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
