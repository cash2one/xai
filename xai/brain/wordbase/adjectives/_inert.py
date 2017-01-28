

#calss header
class _INERT():
	def __init__(self,): 
		self.name = "INERT"
		self.definitions = [u'not moving or not able to move: ', u'not energetic or interesting: ', u'Inert substances do not produce a chemical reaction when another substance is added: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
