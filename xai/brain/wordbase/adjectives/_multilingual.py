

#calss header
class _MULTILINGUAL():
	def __init__(self,): 
		self.name = "MULTILINGUAL"
		self.definitions = [u'(of people or groups) able to use more than two languages for communication, or (of a thing) written or spoken in more than two different languages: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
