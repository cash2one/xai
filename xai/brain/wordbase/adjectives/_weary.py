

#calss header
class _WEARY():
	def __init__(self,): 
		self.name = "WEARY"
		self.definitions = [u'very tired, especially after working hard for a long time: ', u'bored with something because you have experienced too much of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
