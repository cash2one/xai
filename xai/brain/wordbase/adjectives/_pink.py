

#calss header
class _PINK():
	def __init__(self,): 
		self.name = "PINK"
		self.definitions = [u'of a pale red colour: ', u'(slightly) supporting socialist ideas and principles', u'relating to gay people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
