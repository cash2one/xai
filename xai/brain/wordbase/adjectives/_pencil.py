

#calss header
class _PENCIL():
	def __init__(self,): 
		self.name = "PENCIL"
		self.definitions = [u'used to describe something that has been drawn with a pencil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
