

#calss header
class _IMPOLITIC():
	def __init__(self,): 
		self.name = "IMPOLITIC"
		self.definitions = [u'If words or actions are impolitic, they are unwise and likely to cause offence or problems, especially in social situations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
