

#calss header
class _BILINGUAL():
	def __init__(self,): 
		self.name = "BILINGUAL"
		self.definitions = [u'(of a person) able to use two languages equally well, or (of a thing) using or involving two languages: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
