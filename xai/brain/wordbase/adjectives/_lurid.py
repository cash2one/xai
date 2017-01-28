

#calss header
class _LURID():
	def __init__(self,): 
		self.name = "LURID"
		self.definitions = [u'(especially of a description) shocking because involving violence, sex, or immoral activity: ', u'too brightly coloured: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
