

#calss header
class _FATAL():
	def __init__(self,): 
		self.name = "FATAL"
		self.definitions = [u'A fatal illness, accident, etc. causes death: ', u'very serious and having an important bad effect in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
