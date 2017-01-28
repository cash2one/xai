

#calss header
class _SLUSHY():
	def __init__(self,): 
		self.name = "SLUSHY"
		self.definitions = [u'Slushy snow is partly melted.', u'Slushy language is too emotional and romantic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
