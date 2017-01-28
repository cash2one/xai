

#calss header
class _GRAPHIC():
	def __init__(self,): 
		self.name = "GRAPHIC"
		self.definitions = [u'very clear and powerful: ', u'related to drawing or printing: ', u'relating to, using, or consisting of a graph or graphs']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
