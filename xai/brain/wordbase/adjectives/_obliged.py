

#calss header
class _OBLIGED():
	def __init__(self,): 
		self.name = "OBLIGED"
		self.definitions = [u'to be forced to do something or feel that you must do something: ', u'used to thank someone and say that you are grateful: ', u'used to ask someone politely to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
