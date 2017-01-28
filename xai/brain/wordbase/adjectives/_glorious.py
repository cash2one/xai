

#calss header
class _GLORIOUS():
	def __init__(self,): 
		self.name = "GLORIOUS"
		self.definitions = [u'deserving great admiration, praise, and honour: ', u'very beautiful: ', u'Glorious weather is very pleasant, and especially hot and sunny: ', u'very enjoyable or giving great pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
