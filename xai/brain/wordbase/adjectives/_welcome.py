

#calss header
class _WELCOME():
	def __init__(self,): 
		self.name = "WELCOME"
		self.definitions = [u'If someone is welcome, you are pleased when they visit you: ', u'to show someone that you are pleased that they are with you: ', u'If something is welcome, you are pleased to have or do it: ', u'used to tell someone that they can certainly do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
