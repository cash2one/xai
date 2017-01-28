

#calss header
class _SOLID():
	def __init__(self,): 
		self.name = "SOLID"
		self.definitions = [u'hard or firm, keeping a clear shape: ', u'completely hard or firm all through an object, or without any spaces or holes: ', u'A solid metal or colour is pure and does not have anything else mixed together with it: ', u'not liquid or gas: ', u'Solid food is not in liquid form, especially when given to babies or people who are ill: ', u'certain or safe; of a good standard; giving confidence or support: ', u'continuing for a period of time without stopping: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
