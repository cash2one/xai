

#calss header
class _CLOSETED():
	def __init__(self,): 
		self.name = "CLOSETED"
		self.definitions = [u'A closeted gay man or woman keeps the fact that he or she is gay secret from most people: ', u'used to describe an activity or opinion that someone keeps secret: ', u'If someone is closeted somewhere, they stay there, often because they are working hard on something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
