

#calss header
class _ILL():
	def __init__(self,): 
		self.name = "ILL"
		self.definitions = [u'not feeling well, or suffering from a disease: ', u'bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
