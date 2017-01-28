

#calss header
class _ATTENTIVE():
	def __init__(self,): 
		self.name = "ATTENTIVE"
		self.definitions = [u'listening carefully: ', u'If someone is attentive, they are very helpful and take care of you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
