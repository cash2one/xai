

#calss header
class _UNWASHED():
	def __init__(self,): 
		self.name = "UNWASHED"
		self.definitions = [u'not washed: ', u'a humorous or insulting way to refer to ordinary, uneducated or poor people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
