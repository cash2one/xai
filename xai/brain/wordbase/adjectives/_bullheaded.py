

#calss header
class _BULLHEADED():
	def __init__(self,): 
		self.name = "BULLHEADED"
		self.definitions = [u"very determined to do what you want to do, especially without considering other people's feelings"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
