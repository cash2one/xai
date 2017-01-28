

#calss header
class _TRANSLUCENT():
	def __init__(self,): 
		self.name = "TRANSLUCENT"
		self.definitions = [u'If an object or a substance is translucent, it is almost transparent, allowing some light through it in an attractive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
