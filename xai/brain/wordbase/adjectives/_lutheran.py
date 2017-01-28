

#calss header
class _LUTHERAN():
	def __init__(self,): 
		self.name = "LUTHERAN"
		self.definitions = [u'of or relating to the part of Protestant Christianity that is based on the ideas of the German religious leader Martin Luther: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
