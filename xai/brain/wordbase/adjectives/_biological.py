

#calss header
class _BIOLOGICAL():
	def __init__(self,): 
		self.name = "BIOLOGICAL"
		self.definitions = [u'connected with the natural processes of living things: ', u'related by birth: ', u'used to describe a substance used for cleaning that uses enzymes to remove dirt: ', u'using living matter, such as bacteria, to seriously harm and kill people and animals, and to damage crops: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
