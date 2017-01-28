

#calss header
class _ABSENT():
	def __init__(self,): 
		self.name = "ABSENT"
		self.definitions = [u'not in the place where you are expected to be, especially at school or work: ', u'not existing: ', u"used to describe a person or the expression on a person's face when they are thinking about other things and are not paying attention to what is happening near them"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
