

#calss header
class _DISCONNECTED():
	def __init__(self,): 
		self.name = "DISCONNECTED"
		self.definitions = [u'If ideas, remarks, etc. or the different parts of something are disconnected, they are not well joined together and it is difficult to see their purpose or pattern: ', u'A disconnected hairstyle is one in which some parts, usually at the sides, have been cut very short and other parts, usually on top, are fairly long.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
