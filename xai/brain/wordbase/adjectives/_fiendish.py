

#calss header
class _FIENDISH():
	def __init__(self,): 
		self.name = "FIENDISH"
		self.definitions = [u'evil and cruel: ', u'clever and difficult, sometimes in a bad way: ', u'very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
