

#calss header
class _LITERATE():
	def __init__(self,): 
		self.name = "LITERATE"
		self.definitions = [u'able to read and write', u'having knowledge of a particular subject, or a particular type of knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
